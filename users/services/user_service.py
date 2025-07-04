from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import transaction
from ..serializers import UserSerializers
from ..models import User

class UserService:
    @staticmethod
    @transaction.atomic
    def create_user(data):
        serializer = UserSerializers(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.save()

    @staticmethod
    @transaction.atomic
    def assign_user_to_group(user_id, group_id):
        try:
            user = User.objects.get(pk=user_id)
            group = Group.objects.get(pk=group_id)
        except ObjectDoesNotExist:
            raise ValidationError("Foydalanuvchi yoki gruh topilmadi")

        user.groups.add(group)
        user.save()
        return user

    @staticmethod
    @transaction.atomic
    def deactivate_user(user_id):
        try:
            user = User.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            raise ValidationError("Foydaluvchi topilmadi")

        user.is_active = False
        user.save()

        return user

    @staticmethod
    @transaction.atomic
    def change_email(user_id, new_email):
        if not new_email or not '@' in new_email or not '.' in new_email:
            raise ValidationError("Email xato")

        try:
            user = User.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            raise ValidationError("Foydaluvchi topilmadi")

        user.email = new_email
        user.full_clean()
        user.save()

        return user

