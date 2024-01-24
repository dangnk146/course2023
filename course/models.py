from django.db import models
from users.models import TeacherUser, StudentUser

class Factory(models.Model):
    name = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ClassMembership(models.Model):
    name = models.CharField(max_length=20, null=True)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100, null=True)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, null=True)
    image = models.FileField(null=True, blank=True)
    teacher = models.ForeignKey(TeacherUser, on_delete=models.CASCADE, null=True, blank=True)
    class_membership = models.ForeignKey(ClassMembership, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class MembershipStudentUser(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    class_membership = models.ForeignKey(ClassMembership, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE, null=True, blank=True)

class MembershipTeacherUser(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    class_membership = models.ForeignKey(ClassMembership, on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherUser, on_delete=models.CASCADE, null=True, blank=True)

class Tag(models.Model):
    name = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=30, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ChuongTag(models.Model):
    name = models.CharField(max_length=400, null=True)
    description = models.CharField(max_length=800, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Lession(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.FileField(null=True, blank=True)
    baigiangtuongtac = models.FileField(null=True, blank=True)
    pptx = models.FileField(null=True, blank=True)
    pdf = models.FileField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    chuongTag = models.ForeignKey(ChuongTag, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class TagLessionCourse(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)
    lession = models.ForeignKey(Lession, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tag.name if self.tag else ''

class LessionExam(models.Model):
    name = models.CharField(max_length=100, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)
    image = models.FileField(null=True, blank=True)
    baigiangtuongtac = models.FileField(null=True, blank=True)
    pptx = models.FileField(null=True, blank=True)
    pdf = models.FileField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    timestart = models.DateTimeField(null=True, blank=True)
    timeend = models.DateTimeField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    chuongTag = models.ForeignKey(ChuongTag, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class LessionTracNghiem(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=800, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    chuongTag = models.ForeignKey(ChuongTag, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class LessionSubTracNghiem(models.Model):
    nametracnghiem = models.CharField(max_length=100, null=True)
    solutionA = models.CharField(max_length=100, null=True)
    solutionB = models.CharField(max_length=100, null=True)
    solutionC = models.CharField(max_length=100, null=True)
    solutionD = models.CharField(max_length=100, null=True)
    solutionTrue = models.CharField(max_length=100, null=True)
    vitrisapxep = models.IntegerField(null=True, blank=True)
    lessionTracNghiem = models.ForeignKey(LessionTracNghiem, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nametracnghiem

class TagLessionExameCourse(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)
    lessionexam = models.ForeignKey(LessionExam, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.tag.name if self.tag else ''

class Result(models.Model):
    result = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    lessionexam = models.ForeignKey(LessionExam, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(StudentUser, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.result

class SubmitLessionExam(models.Model):
    user = models.ForeignKey(StudentUser, on_delete=models.CASCADE, null=True)
    file = models.FileField(null=True, blank=True)
    result = models.ForeignKey(Result, on_delete=models.CASCADE, null=True)
    lessionexam = models.ForeignKey(LessionExam, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
