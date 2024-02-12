# определить класс AuthSystem с методом authenticate_user()

# auth.py
from django.contrib.auth.models import User

class AuthSystem:
    @staticmethod
    def authenticate_user(username, password):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
