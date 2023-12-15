from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from course.models import *
from django.contrib.auth.models import User

def GetDataUser(user):
    try:
        data = TeacherUser.objects.get(user=user)
        return data
    except:
        pass
    try:
        data = StudentUser.objects.get(user=user)
        return data
    except:
        pass

def CheckRole(user):
    isRole = False
    result = 'notrole'
    if (user):
        try:
            data = TeacherUser.objects.get(user=user)
            if data:
                result = 'teacher'
        except:
            isRole = True

        try:
            data = StudentUser.objects.get(user=user)
            if data:
                result = 'student'
        except:
            isRole = True
    return result



def GetUser(user):    
    # If user is teacher
    try:
        data = TeacherUser.objects.get(user=user)
        if data:
            return data
    except:
        pass

    try:
        data = StudentUser.objects.get(user=user)
        if data:
            return data
    except:
        pass

    return None


def Count_inactive_users():
    # Đếm tổng số người dùng chưa được kích hoạt (isActive=False)
    inactive_teacher_count = TeacherUser.objects.filter(isActive=False).count()
    inactive_student_count = StudentUser.objects.filter(isActive=False).count()
    
    total_inactive_users = inactive_teacher_count + inactive_student_count
    return total_inactive_users

# Đếm tổng số TeacherUser
def Count_teacher_users():
    teacher_count = TeacherUser.objects.count()
    return teacher_count

# Đếm tổng số StudentUser
def Count_student_users():
    student_count = StudentUser.objects.count()
    return student_count

# Đếm tổng số ClassMembership
def Count_class_memberships():
    class_membership_count = ClassMembership.objects.count()
    return class_membership_count

def Get_inactive_teachers():
    inactive_teachers = TeacherUser.objects.filter(isActive=False)
    
    return inactive_teachers

def Get_inactive_students():
    inactive_students = StudentUser.objects.filter(isActive=False)    
    return inactive_students

def Get_active_teachers():
    active_teachers = TeacherUser.objects.filter(isActive=True)
    
    return active_teachers

def Get_active_students():
    active_students = StudentUser.objects.filter(isActive=True)
    
    return active_students

def UserInClassAddById(user_type, user_id, classroom_id):
    if user_type == 'student':
        classroom = get_object_or_404(ClassMembership, id=classroom_id)
        student = get_object_or_404(StudentUser, id=user_id)
        factory = get_object_or_404(Factory, id=classroom.factory.id)
        MembershipStudentUser.objects.create(class_membership=classroom, student=student, factory= factory)
    if user_type == 'teacher':
        classroom = get_object_or_404(ClassMembership, id=classroom_id)
        teacher = get_object_or_404(TeacherUser, id=user_id)
        factory = get_object_or_404(Factory, id=classroom.factory.id)
        MembershipTeacherUser.objects.create(class_membership=classroom, teacher=teacher, factory= factory)

def UserInClassUpdateById(user_type, user_id, classroom_id, classroom_id_new):
    if user_type == 'teacher':
        classroom = get_object_or_404(ClassMembership, id=classroom_id)
        teacher = get_object_or_404(TeacherUser, id=user_id)
        if classroom and teacher:
            teacher_membership = MembershipTeacherUser.objects.filter(class_membership=classroom, teacher=teacher).first()
            if teacher_membership:
                classroom = get_object_or_404(ClassMembership, id=classroom_id_new)
                teacher_membership.class_membership= classroom
                teacher_membership.save()

def DeleteUserInClassUpdateById(user_type, teacher, classroom):
    print(classroom.id)    
    print("classroom.id")   
    print(teacher.id)    
    print("teacher.id")   
    print("-----------------------------------------------------")    
    teacher_memberships = MembershipTeacherUser.objects.filter(class_membership=classroom, teacher=teacher).first()  
    print(teacher_memberships.id)    
    print("teacher_memberships.id")    
    print("-----------------------------------------------------")    

    teacher_memberships.delete()


def Add_user_Teacher_in_class_by_email(email):
    newuser=TeacherUser.objects.filter(user__email=email).first()
    return newuser

def User_Teacher_in_class_by_user(user):
    newuser=TeacherUser.objects.filter(user=user).first()
    return newuser

def Add_user_Student_in_class_by_email(email):
    newuser=StudentUser.objects.filter(user__email=email).first()
    return newuser