from .models import *

def Count_factory():
    count_factory = Factory.objects.count()
    return count_factory

def Count_course():
    count_course = Course.objects.count()
    return count_course

def Count_course_student_memberships(class_membership):
    course = Course.objects.filter(class_membership=class_membership)
    return course

def GetMembershipTeacherUser(data):
    try:
        class_membership = MembershipTeacherUser.objects.get(teacher=data)
        if class_membership:
            return True
    except:        
        return False