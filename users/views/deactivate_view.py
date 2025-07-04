from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.services import UserService

class DeactivateUserAPIView(APIView):
    def post(self, request):
        try:
            user = UserService.assign_user_to_group(request.data["user_id"])
            return Response({"message": f"{user.username} gruppaga qo‘shildi"})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_201_CREATED)
