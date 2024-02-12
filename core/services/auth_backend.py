from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # Try to find the user by email
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            try:
                # Try to find the user by username
                user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                try:
                    # Try to find the user by phone
                    user = UserModel.objects.get(phone=username)
                except UserModel.DoesNotExist:
                    return None

        if user.check_password(password):
            return user
        return None
    
