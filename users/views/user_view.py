from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.repositories.user_repository import UserRepository
from users.selectors import UserSelectors
from users.services import UserService
from users.serializers import UserSerializers

class UserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')

        if user_id:
            user_qs = UserRepository.get_by_id(user_id)
            if not user_qs.exists():
                return Response({"error": "Foydalanuvchi topilmadi"}, status=status.HTTP_404_NOT_FOUND)
            serializer = UserSerializers(user_qs.first())
            return Response(serializer.data())
        else:
            users = UserSelectors.get_active_users()
            serializer = UserSerializers(users, many=True)
            return Response(serializer.data())

    def post(self, request):
        user = UserService.create_user()
        serializer = UserSerializers(user)
        return Response(serializer.data(), status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user_qs = UserRepository.get_by_id(user_id)

        if not user_qs.exists():
            return Response({"error": "Foydalanuvchi mavjud emas"}, status=status.HTTP_404_NOT_FOUND)

        user = user_qs.first()
        serializer = UserSerializers(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user_qs = UserRepository.get_by_id(user_id)

        if not user_qs.exists():
            return Response({"error": "Foydalanuvchi mavjud emas"}, status=status.HTTP_404_NOT_FOUND)

        UserRepository.delete(user_qs.first())
        return Response(status=status.HTTP_202_ACCEPTED)

