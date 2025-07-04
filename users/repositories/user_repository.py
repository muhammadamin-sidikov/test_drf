from ..models import User

class UserRepository:
    @staticmethod
    def get_by_id(id):
        return User.objects.filter(id=id)

    @staticmethod
    def get_all():
        return User.objects.all()

    @staticmethod
    def filter_by_criteria(**kwargs):
        return User.objects.filter(**kwargs)

    @staticmethod
    def save(user):
        user.save()

    @staticmethod
    def delete(user):
        user.delete()

