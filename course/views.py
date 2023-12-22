from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User

from .models import *
from users.models import *

from users.helper import *
from .helper import *

 

# Create your views here.
def ManageCourse(request):
    user = User.objects.get(username=request.user.username)
    
    data = GetUser(user)
    count_factory = Count_factory()
    count_course = Count_course()
    
    d = {'data': data, 'count_factory': count_factory, 'count_course': count_course}
    return render(request, 'dashboardCourse.html', d)

def ManageCourseFactory(request):
    if request.method == "GET":
        user = User.objects.get(username=request.user.username)
        data = GetUser(user)

        factories = Factory.objects.all()
        d = {'data': data, 'factories': factories }
        return render(request, 'manageFactory.html', d)
    if request.method == "POST":
        factory = request.POST["factory"]
        if (factory):
            Factory.objects.create(name=factory)
            return redirect('manageCourseFactory')
        return redirect('manageCourseFactory')


def ManageCourseFactoryEdit(request, pid):
    user = User.objects.get(username=request.user.username)
    
    factory = get_object_or_404(Factory, id=pid)
    if request.method == "GET":
        data = GetUser(user)
        d = {'data': data, 'factory': factory}
        return render(request, 'manageFactoryEdit.html', d)
    if request.method == "POST":
        new_factory_name  = request.POST['factory']
        factory.name = new_factory_name
        factory.save()  # Save the changes to the database

        return redirect('manageCourseFactory')

def ManageCourseFactoryDelete(request, pid):
    factory = get_object_or_404(Factory, id=pid)
    factory.delete()
    return redirect('manageCourseFactory')


def ManageCourseCourse(request):
    user = User.objects.get(username=request.user.username)
    data = GetUser(user)
    factories = Factory.objects.all()
    result=''
    
    if request.method == "GET":

        d = {'data': data, 'factories': factories, 'result':result }
        return render(request, 'manageCourse.html', d)
    if request.method == "POST":
        factory_id  = request.POST['factory']
        name_course  = request.POST['course']
        if request.FILES:
            image = request.FILES['image']
        factory = get_object_or_404(Factory, id=factory_id)
        result = 'fail'
        if (factory and name_course):
            if request.FILES:
                Course.objects.create(name=name_course, factory=factory)
            else:
                Course.objects.create(name=name_course, factory=factory, image=image)
            result = 'success'
        return redirect('manageCourseCourse')

def ManageCourseCourseDetail(request, pid): 
    user = User.objects.get(username=request.user.username)
    data = GetUser(user)
    factory = get_object_or_404(Factory, id=pid)
    class_membership = ClassMembership.objects.all()
    courses = Course.objects.filter(factory=factory)
    if request.method == "GET":
        d = {'data': data, 'factory': factory, 'courses': courses, 'class_membership': class_membership }
        return render(request, 'manageCourseDetail.html', d)
    if request.method == "POST":
        factory_id  = request.POST['factory']
        name_course  = request.POST['course']
        email  = request.POST['email']
        image = request.FILES['image']

        classroom = request.POST['classroom']
        class_membership = get_object_or_404(ClassMembership, id=classroom)

        factory = get_object_or_404(Factory, id=factory_id)
        result = 'fail'
        teacher = Add_user_Teacher_in_class_by_email(email)
        
        if (factory and name_course and teacher):
            new_courses = Course.objects.create(name=name_course, teacher=teacher, factory=factory, image= image, class_membership= class_membership)
            result = 'success'
            UserInClassAddById('teacher', teacher.id, new_courses.class_membership.id)
        return redirect('manageCourseCourseDetail', pid)
        

def ManageCourseCourseEdit(request, pid):
    user = User.objects.get(username=request.user.username)
    data = GetUser(user)
    course = get_object_or_404(Course, id=pid)
    factory = course.factory
    class_membership = ClassMembership.objects.all()
    classmembership = get_object_or_404(ClassMembership, id=course.class_membership.id)
    
    image = None  # Initialize image as None

    if request.method == "GET":
        d = {'data': data, 'factory': factory, 'course': course, 'class_membership': class_membership, 'classmembership': classmembership}
        return render(request, 'manageCourseEdit.html', d)

    if request.method == "POST":
        factory = request.POST['factory']
        classmembership = request.POST['classmembership']
        name_course = request.POST['course']

        if 'image' in request.FILES:  # Check if 'image' is in request.FILES
            image = request.FILES['image']  # Assign image if available

        if name_course and name_course != course.name:
            course.name = name_course

        if image and course.image != image:
            course.image = image
        classroom_id = course.class_membership.id
        if factory and course.factory.id != factory:
            course.factory = get_object_or_404(Factory, id=factory)
        if classmembership and course.class_membership.id != classmembership:
            course.class_membership = get_object_or_404(ClassMembership, id=classmembership)
            teacher = User_Teacher_in_class_by_user(user)
            UserInClassUpdateById('teacher', teacher.id, classroom_id, course.class_membership.id)

        course.save()
        return redirect('manageCourseCourseDetail', course.factory.id)



def ManageCourseCourseDelete(request, pid):
    user = User.objects.get(username=request.user.username)    
    course = get_object_or_404(Course, id=pid)
    factory = course.factory

    teacher = course.teacher
    classroom = course.class_membership
    DeleteUserInClassUpdateById('teacher', teacher, classroom)
    course.delete()
    return redirect('manageCourseCourseDetail', factory.id)


def ManageTag(request):
    if request.method == "GET":
        user = User.objects.get(username=request.user.username)
        
        data = GetUser(user)
        tags = Tag.objects.all()
        
        d = {'data': data, 'tags': tags}
        return render(request, 'dashboardCourseTag.html', d)
    if request.method == "POST":
        tag = request.POST["tag"]
        description = request.POST["description"]
        Tag.objects.create(name=tag, description=description)
        return redirect('manageTag')



def ManageTagEdit(request, pid):
    if request.method == "GET":
        user = User.objects.get(username=request.user.username)
        
        data = GetUser(user)
        
        tag = Tag.objects.get(id=pid)
        d = {'data': data, 'tag': tag}
        return render(request, 'dashboardCourseTagEdit.html', d)
    if request.method == "POST":
        tag = Tag.objects.get(id=pid)
        name = request.POST["name"]
        description = request.POST["description"]

        if tag.name != name:
            tag.name=name
        if tag.description != description:
            tag.description=description
        tag.save()
        return redirect('manageTag')

def ManageTagDelete(request, pid):
    tag = Tag.objects.get(id=pid)
    tag.delete()
    return redirect('manageTag')