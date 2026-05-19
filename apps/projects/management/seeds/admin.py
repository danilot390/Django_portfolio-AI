from decouple import config
from django.contrib.auth import get_user_model


def seed_admin(stdout=None):
    User = get_user_model()

    username = config("ADMIN_USERNAME", cast=str)
    email = config("ADMIN_EMAIL", cast=str)
    password = config("ADMIN_PASSWORD", cast=str)

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )

        if stdout:
            stdout.write(
                f"Admin user '{username}' created."
            )