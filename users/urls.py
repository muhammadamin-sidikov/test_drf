from django.urls import path
from .views import (
    UserAPIView,
    AssignToGroupAPIView,
    DeactivateUserAPIView,
    ChangeEmailAPIView,
)

urlpatterns = [
    path("users/", UserAPIView.as_view()),
    path("users/<int:pk>/", UserAPIView.as_view()),
    path("users/assign_to_group/", AssignToGroupAPIView.as_view()),
    path("users/deactivate/", DeactivateUserAPIView.as_view()),
    path("users/change_email/", ChangeEmailAPIView.as_view()),
]