from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.services import UserService

class AssignToGroupAPIView(APIView):
    def post(self, request):
        try:
            user = UserService.assign_user_to_group(request.data['user_id'], request.data['group_id'])
            return Response({'massage': f'{user.username} gruppaga qo‘shildi'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
