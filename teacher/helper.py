from course.models import *
from course.helper import *
from users.models import *
from users.helper import *

def Get_class_membershipss(teacher):
    class_memberships = MembershipTeacherUser.objects.filter(teacher=teacher)
    class_membershipss = []

    for class_membership in class_memberships:
        # Kiểm tra xem class_membership đã tồn tại trong danh sách class_membershipss chưa
        if class_membership.class_membership not in class_membershipss:
            class_membershipss.append(class_membership.class_membership)

    return class_membershipss

def Get_student_class_membershipss(selected_class_id):
    classroom = get_object_or_404(ClassMembership, id=selected_class_id)
    student_memberships = MembershipStudentUser.objects.filter(class_membership=classroom)
    students = [membership.student for membership in student_memberships]
    return students

def Get_course_teacher_class_membershipss(data, class_membership):
    courses = Course.objects.filter(teacher=data, class_membership=class_membership)
    return courses