from django.db import models
from users.models import *


# Create your models here.
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
    image = models.FileField(null=True)
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

    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Lession(models.Model):
    name = models.CharField(max_length=100, null=True)
    
    image =  models.FileField(null=True, blank=True)
    baigiangtuongtac = models.FileField(null=True, blank=True)
    pptx = models.FileField(null=True, blank=True)
    pdf = models.FileField(null=True, blank=True)

    content = models.TextField(null=True, blank=True)  # Trường TextField để lưu nội dung blog
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True)

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
        return self.name


class LessionExam(models.Model):
    name = models.CharField(max_length=100, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)
    
    image =  models.FileField(null=True, blank=True)
    baigiangtuongtac = models.FileField(null=True, blank=True)
    pptx = models.FileField(null=True, blank=True)
    pdf = models.FileField(null=True, blank=True)

    content = models.TextField(null=True, blank=True)  # Trường TextField để lưu nội dung blog
    
    timestart = models.DateTimeField(null=True, blank=True)
    timeend = models.DateTimeField(null=True, blank=True)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True)

    chuongTag = models.ForeignKey(ChuongTag, on_delete=models.CASCADE, null=True)
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class LessionTracNghiem(models.Model):
    name = models.CharField(max_length=100, null=True) # Tên bộ đề
    description = models.CharField(max_length=800, null=True, blank=True)    
    
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True)

    chuongTag = models.ForeignKey(ChuongTag, on_delete=models.CASCADE, null=True)
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class LessionSubTracNghiem(models.Model):
    nametracnghiem = models.CharField(max_length=100, null=True) # Câu hỏi
    solutionA=models.CharField(max_length=100, null=True)# Đáp án A
    solutionB=models.CharField(max_length=100, null=True)# Đáp án B
    solutionC=models.CharField(max_length=100, null=True)# Đáp án C
    solutionD=models.CharField(max_length=100, null=True) # Đáp án D

    solutionTrue=models.CharField(max_length=100, null=True) # Đáp án đúng

    

    vitrisapxep=models.IntegerField(max_length=100, null=True, blank=True) # Vị trí cửa câu hỏi trong danh sách câu trắc nghiệm
    
    lessionTracNghiem = models.ForeignKey(
        LessionTracNghiem, on_delete=models.CASCADE, null=True)
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class TagLessionExameCourse(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)
    lessionexam = models.ForeignKey(LessionExam, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Result(models.Model):
    result = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)

    lessionexam = models.ForeignKey(LessionExam, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(StudentUser, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.result

# Participant
class SubmitLessionExam(models.Model):
    user = models.ForeignKey(StudentUser, on_delete=models.CASCADE, null=True)
    file = models.FileField(null=True, blank=True)
    result = models.ForeignKey(Result, on_delete=models.CASCADE, null=True)
    
    lessionexam = models.ForeignKey(LessionExam, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

