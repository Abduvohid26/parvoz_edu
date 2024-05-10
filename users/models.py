import uuid
import random
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken

STUDENT, TEACHER, SEO, ADMIN, MANAGER = ('student', 'teacher', 'seo', 'admin', 'manager')


class User(AbstractUser):
    USER_STATUS = (
        (ADMIN, ADMIN),
        (MANAGER, MANAGER),
        (SEO, SEO),
        (TEACHER, TEACHER),
        (STUDENT, STUDENT)
    )
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    phone_number = models.CharField(max_length=14, null=True, blank=True)
    status = models.CharField(max_length=50, choices=USER_STATUS, default=STUDENT)
    created_at = models.DateTimeField(default=timezone.now)

    def check_username(self):
        if not self.username:
            temp_username = f'parvoz-{uuid.uuid4().__str__().split("-")[-1]}'
            while User.objects.filter(username=temp_username):
                temp_username = f"{temp_username}{random.randint(0, 9)}"
            self.username = temp_username

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def token(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh_token': str(refresh),
            'access_token': str(refresh.access_token),
        }

    def check_hash_password(self):
        if not self.password.startswith('pbkdf2_sha256'):
            return self.set_password(self.password)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.check_hash_password()
        self.check_username()
        super(User, self).save(*args, **kwargs)


class Teachers(models.Model):
    id = models.UUIDField(editable=False, unique=True, primary_key=True, default=uuid.uuid4)
    teacher = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teachers')
    group_qty = models.IntegerField()


class Courses(models.Model):
    id = models.UUIDField(editable=False, unique=True, primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Rooms(models.Model):
    id = models.UUIDField(editable=False, unique=True, primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Groups(models.Model):
    id = models.UUIDField(editable=False, unique=True, primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher_groups')
    days = models.DateTimeField()
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='room_groups')
    student_qty = models.IntegerField()

    def __str__(self):
        return self.name
