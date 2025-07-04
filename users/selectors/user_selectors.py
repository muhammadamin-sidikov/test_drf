from ..models import User

class UserSelectors:
    @staticmethod
    def get_active_users():
        return User.objects.filter(is_acive=True)

    @staticmethod
    def get_top_users_by_score(limit=10):
        return User.objects.order_by('-score')[:limit]
