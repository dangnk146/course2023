from django.shortcuts import render

from course.models import *
from course.helper import *
from users.models import *
from users.helper import *
from teacher.helper import *
from .helper import *
from django.urls import reverse
from django.utils import timezone

# Create your views here.
def ManageStudent(request):
    user = User.objects.get(username=request.user.username)
    data = GetUser(user)

    class_membership = ''
    if(GetMembershipStudentUser(data)):
        class_membership = MembershipStudentUser.objects.get(student=data)
    else:
        url = reverse('home') + '?alert=notsetclass'
        return redirect(url)
    courses = Count_course_student_memberships(class_membership.class_membership)
    course_count = courses.count()

    d = {'data': data, 'class_membership':class_membership, 'courses': courses, 'course_count': course_count}
    return render(request, 'dashboardStudent.html', d)

def ManageStudentCourse(request, id_course):
    user = User.objects.get(username=request.user.username)
    data = GetUser(user)

    class_membership = ''
    if(GetMembershipStudentUser(data)):
        class_membership = MembershipStudentUser.objects.get(student=data)
    else:
        url = reverse('home') + '?alert=notsetclass'
        return redirect(url)
    courses = Count_course_student_memberships(class_membership.class_membership)
    course = get_object_or_404(Course, id=id_course)
    list_lession = TagLessionCourse.objects.filter(course=course)
    list_exam_lession = TagLessionExameCourse.objects.filter(course=course)
    tags = ChuongTag.objects.filter(course=course).order_by('created_at')

    taglessioncourses= Lession.objects.filter(course=course)
    taglessionexamcourses= LessionExam.objects.filter(course=course)
    

    d = {'data': data, 'class_membership':class_membership, 'courses': courses, 'course': course, 'list_lession':list_lession, 'list_exam_lession': list_exam_lession, 'tags': tags, 'taglessioncourses':taglessioncourses, 'taglessionexamcourses': taglessionexamcourses}
    return render(request, 'dashboardStudentCourseId.html', d)

def ManageStudentCourseLession(request, id_course, id_lession):
    user = User.objects.get(username=request.user.username)
    data = GetUser(user)

    class_membership = ''
    if(GetMembershipStudentUser(data)):
        class_membership = MembershipStudentUser.objects.get(student=data)
    else:
        url = reverse('home') + '?alert=notsetclass'
        return redirect(url)
    courses = Count_course_student_memberships(class_membership.class_membership)
    course = get_object_or_404(Course, id=id_course)
    
    lession = Lession.objects.get(id=id_lession)

    d = {'data': data, 'class_membership':class_membership, 'courses': courses, 'course': course, 'lession': lession}
    return render(request, 'dashboardStudentCourseLessionId.html', d)

def ManageStudentCourseLessionExam(request, id_course, id_lession):
    if request.method == "GET":
        user = User.objects.get(username=request.user.username)
        data = GetUser(user)

        class_membership = ''
        
        if(GetMembershipStudentUser(data)):
            class_membership = MembershipStudentUser.objects.get(student=data)
        else:
            result = 'student'
            d = {'result': result, 'data': data, 'alert': 'notsetclass'}
            return redirect('home')
        courses = Count_course_student_memberships(class_membership.class_membership)
        course = get_object_or_404(Course, id=id_course)
        
        lessionExam = LessionExam.objects.get(id=id_lession)
        submitLessionExam = SubmitLessionExam.objects.filter(user=data, lessionexam=lessionExam).first()
        
        
        current_time = timezone.localtime(timezone.now())
        lessionExamStart = timezone.localtime(lessionExam.timestart)
        lessionExamEnd = timezone.localtime(lessionExam.timeend)

        isShow = lessionExamStart <= current_time <= lessionExamEnd

        d = {'data': data, 'current_time': current_time, 'class_membership':class_membership, 'courses': courses, 'course': course, 'lessionExam': lessionExam, 'isShow': isShow}
        if submitLessionExam:
            d = {'data': data, 'current_time': current_time, 'class_membership':class_membership, 'courses': courses, 'course': course, 'lessionExam': lessionExam, 'submitLessionExam': submitLessionExam, 'isShow': isShow}

        return render(request, 'dashboardStudentCourseLessionExamId.html', d)
    if request.method == "POST":
        lessionExam = LessionExam.objects.get(id=id_lession)
        current_time = timezone.now()
        lessionExamStart = timezone.localtime(lessionExam.timestart)
        lessionExamEnd = timezone.localtime(lessionExam.timeend)

        if lessionExamStart <= current_time <= lessionExamEnd:
            user = User.objects.get(username=request.user.username)
            data = GetUser(user)
            file = request.FILES['file']
            lessionExam = LessionExam.objects.get(id=id_lession)
            SubmitLessionExam.objects.create(user=data, file=file, lessionexam=lessionExam)
            return redirect('manageStudentCourseLessonViewExam', id_course, id_lession )
        else:
            # Return a bad request response if the current time is not within the allowed range
            return redirect('manageStudentCourseLessonViewExam', id_course, id_lession )

def ManageStudentCourseLessionExamDeleteSubmit(request, id_course, id_lession, id_submit):
    submitLessionExam = SubmitLessionExam.objects.get(id=id_submit)
    submitLessionExam.delete()
    return redirect('manageStudentCourseLessonViewExam', id_course, id_lession )