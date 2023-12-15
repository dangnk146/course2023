from django.db import models
from django.contrib.auth.models import User




class TeacherUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=10, null=True)
    image = models.FileField(null=True)
    isActive = models.BooleanField(default=False)  # Thêm trường isActive
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_teacher = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class StudentUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=100, null=True)
    image = models.FileField(null=True)
    isActive = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_student = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


