from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.services import UserService

class ChangeEmailAPIView(APIView):
    def post(self, request):
        try:
            user = UserService.change_email(request.data['user_id'], request.data['email'])
            return Response({"message": f"{user.username} email yangilandi", "email": user.email})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)