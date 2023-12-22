from django.shortcuts import render

from course.models import *
from course.helper import *
from users.models import *
from users.helper import *
from users.models import *
from .helper import *
from django.urls import reverse





# Create your views here.
def ManageTeacher(request):
    user = User.objects.get(username=request.user.username)
    data = GetUser(user)
    teacher = get_object_or_404(TeacherUser, id=data.id)
    class_memberships = MembershipTeacherUser.objects.filter(teacher=teacher)
    count_class_membership = class_memberships.count()

    class_membershipss = Get_class_membershipss(teacher)

    d = {'data': data, 'count_class_membership': count_class_membership, 'class_memberships':class_membershipss}
    return render(request, 'dashboardTeacher.html', d)

def AddDanhmuc(request, class_membership_id, pid):
    course = Course.objects.get(id=pid)    
    if request.method == "GET":
        user = User.objects.get(username=request.user.username)        
        data = GetUser(user)
        
        class_membership = get_object_or_404(ClassMembership, id=class_membership_id)
        class_membershipss = Get_class_membershipss(data)
        course = Course.objects.get(id=pid)
        tags = Tag.objects.all().order_by('created_at')

        taglessioncourses= TagLessionCourse.objects.filter(course=course)
        taglessionexamcourses= TagLessionExameCourse.objects.filter(course=course)

        danhmuctag = ChuongTag.objects.filter(course=course)
        d = {'data': data,'danhmuctag': danhmuctag, 'class_membership': class_membership, 'class_memberships': class_membershipss, 'course': course, 'taglessioncourses':taglessioncourses, 'tags':tags, 'taglessionexamcourses': taglessionexamcourses}
        return render(request, 'ThemDanhMucTeacher.html', d)
    if request.method == "POST":
        name = request.POST["tag"]
        description = request.POST["description"]
        if description:
            ChuongTag.objects.create(name=name, description=description, course= course)
        else: 
            ChuongTag.objects.create(name=name, course= course)
        return redirect('manageTeacherClassCourse', class_membership_id, pid)

def SuaDanhmuc(request, class_membership_id, pid, danhmuc_id):
    course = Course.objects.get(id=pid)    
    if request.method == "GET":
        user = User.objects.get(username=request.user.username)        
        data = GetUser(user)
        
        class_membership = get_object_or_404(ClassMembership, id=class_membership_id)
        class_membershipss = Get_class_membershipss(data)
        course = Course.objects.get(id=pid)
        tags = Tag.objects.all().order_by('created_at')

        taglessioncourses= TagLessionCourse.objects.filter(course=course)
        taglessionexamcourses= TagLessionExameCourse.objects.filter(course=course)

        danhmuctag = get_object_or_404(ChuongTag, id=danhmuc_id)
        d = {'data': data,'danhmuctag': danhmuctag, 'class_membership': class_membership, 'class_memberships': class_membershipss, 'course': course, 'taglessioncourses':taglessioncourses, 'tags':tags, 'taglessionexamcourses': taglessionexamcourses}
        return render(request, 'UpdateThemDanhMucTeacher.html', d)
    if request.method == "POST":
        danhmuctag = ChuongTag.objects.get(id=danhmuc_id)
        tag = request.POST["tag"]
        description = request.POST["description"]
        
        if danhmuctag.name != tag:
            danhmuctag.name=tag
        if danhmuctag.description != description:
            danhmuctag.description=description
        danhmuctag.save()
        
        return redirect('manageTeacherClassCourseAddDanhmucccc', class_membership_id, pid)

def XoaDanhmuc(request, class_membership_id, pid, danhmuc_id):
    tag = ChuongTag.objects.get(id=danhmuc_id)
    tag.delete()
    return redirect('manageTeacherClassCourseAddDanhmucccc', class_membership_id, pid)

def ManageTeacherClass(request, pid):
    user = User.objects.get(username=request.user.username)
    data = GetUser(user)
    class_membership = get_object_or_404(ClassMembership, id=pid)
    class_membershipss = Get_class_membershipss(data)

    course_teacher = Get_course_teacher_class_membershipss(data, class_membership)
    
    d = {'data': data,'class_membership': class_membership, 'class_memberships': class_membershipss, 'course_teacher': course_teacher}
    return render(request, 'dashboardTeacherClassId.html', d)

def ManageTeacherClassStudent(request, pid):
    user = User.objects.get(username=request.user.username)
    data = GetUser(user)
    class_membership = get_object_or_404(ClassMembership, id=pid)
    class_membershipss = Get_class_membershipss(data)
    
    get_student_class_memberships =Get_student_class_membershipss(pid)

    d = {'data': data,'class_membership': class_membership, 'class_memberships': class_membershipss, 'get_student_class_memberships': get_student_class_memberships}
    return render(request, 'dashboardTeacherClassIdStudents.html', d)

def ManageTeacherClassCourse(request, class_membership_id, pid):
    user = User.objects.get(username=request.user.username)
    data = GetUser(user)
    class_membership = get_object_or_404(ClassMembership, id=class_membership_id)
    class_membershipss = Get_class_membershipss(data)
    course = Course.objects.get(id=pid)
    tags = ChuongTag.objects.filter(course=course).order_by('created_at')

    taglessioncourses= Lession.objects.filter(course=course)
    taglessionexamcourses= LessionExam.objects.filter(course=course)
    d = {'data': data, 'class_membership': class_membership, 'class_memberships': class_membershipss, 'course': course, 'taglessioncourses':taglessioncourses, 'tags':tags, 'taglessionexamcourses': taglessionexamcourses}
    return render(request, 'dashboardTeacherClassCourseId.html', d)



def ManageTeacherClassCourseLeassonAdd(request, class_membership_id, pid, id_chuong):
    if request.method == "GET":
        user = User.objects.get(username=request.user.username)
        data = GetUser(user)
        class_membership = get_object_or_404(ClassMembership, id=class_membership_id)
        class_membershipss = Get_class_membershipss(data)
        course = Course.objects.get(id=pid)
        chuong = ChuongTag.objects.get(id=id_chuong)
        tags = Tag.objects.all()
        
        d = {'data': data, 'chuong': chuong, 'class_membership': class_membership, 'class_memberships': class_membershipss, 'course': course, 'tags': tags}
        return render(request, 'dashboardTeacherClassCourseLeassonIdAdd.html', d)
    if request.method == "POST":
        name  = request.POST.get('name', '')
        content  = request.POST.get('content', '')
        course = get_object_or_404(Course, id=pid)
        chuongTag = ChuongTag.objects.get(id=id_chuong)

        data = Lession.objects.create(name=name,content=content, course=course, chuongTag=chuongTag)

        try:
            if(request.FILES['image']):
                data.image = request.FILES['image']
        except:
            pass
        try:
            if(request.FILES['baigiangtuongtac']):
                data.baigiangtuongtac = request.FILES['baigiangtuongtac']
        except:
            pass
        try:
            if(request.FILES['pptx']):
                data.pptx = request.FILES['pptx']
        except:
            pass
        try:
            if(request.FILES['pdf']):
                data.pdf = request.FILES['pdf']
        except:
            pass

        data.save()

        
        return redirect('manageTeacherClassCourse', class_membership_id, pid)

def ManageTeacherClassCourseEdit(request, class_membership_id, pid, idlession):
    if request.method == "GET":
        user = User.objects.get(username=request.user.username)
        data = GetUser(user)
        class_membership = get_object_or_404(ClassMembership, id=class_membership_id)
        class_membershipss = Get_class_membershipss(data)
        course = Course.objects.get(id=pid)

        lession = get_object_or_404(Lession, id=idlession)
        
        d = {'data': data, 'class_membership': class_membership, 'class_memberships': class_membershipss, 'course': course, 'lession': lession}
        return render(request, 'dashboardTeacherClassCourseLeassonIdEdit.html', d)
    if request.method == "POST":
        name  = request.POST.get('name', '')
        
        content  = request.POST.get('content', '')
        # course = get_object_or_404(Course, id=pid)

        # tagObject = get_object_or_404(Tag, id=tag)
        lession = get_object_or_404(Lession, id=idlession)
        try:
            if request.FILES['image']:
                lession.image = request.FILES['image']
        except:
            pass
        try:
            if request.FILES['baigiangtuongtac']:
                lession.baigiangtuongtac = request.FILES['baigiangtuongtac']
        except:
            pass
        try:
            if request.FILES['pptx']:
                lession.pptx = request.FILES['pptx']
        except:
            pass
        try:
            if request.FILES['pdf']:
                lession.pdf = request.FILES['pdf']
        except:
            pass
        if lession:
            if name and name!= lession.name:
                lession.name = name           
            if content and content!= lession.content:
                lession.content = content
            lession.save()

        return redirect('manageTeacherClassCourse', class_membership_id, pid)
    
def ManageTeacherClassCourseDelete(request, class_membership_id, pid, idlession):
    lession = get_object_or_404(Lession, id=idlession)
    lession.delete()
    return redirect('manageTeacherClassCourse', class_membership_id, pid)


def ManageTeacherClassCourseLessionView(request, class_membership_id, id_course, id_lession):
    user = User.objects.get(username=request.user.username)
    data = GetUser(user)
    teacher = get_object_or_404(TeacherUser, id=data.id)

    class_membership = ''
    class_membership = MembershipTeacherUser.objects.get(teacher=data)

    courses = Count_course_student_memberships(class_membership.class_membership)
    course = get_object_or_404(Course, id=id_course)
    
    lession = Lession.objects.get(id=id_lession)

    class_memberships = Get_class_membershipss(teacher)

    
    d = {'data': data,'class_memberships': class_memberships, 'class_membership':class_membership.class_membership, 'courses': courses, 'course': course, 'lession': lession}

    return render(request, 'dashboardTeacherCourseLessionIdView.html', d)

def ManageTeacherClassCourseLessionExamView(request, class_membership_id, id_course, id_lession):
    user = User.objects.get(username=request.user.username)
    data = GetUser(user)
    # teacher = get_object_or_404(TeacherUser, id=data.id)

    class_membership = ''
    if(GetMembershipTeacherUser(data)):
        class_membership = MembershipTeacherUser.objects.get(teacher=data)
    else:
        url = reverse('home') + '?alert=notsetclass'
        return redirect(url)

    courses = Count_course_student_memberships(class_membership.class_membership)
    course = get_object_or_404(Course, id=id_course)

    class_memberships = Get_class_membershipss(data)
    
    
    
    lessionExam = LessionExam.objects.get(id=id_lession)
    submitLessionExams = SubmitLessionExam.objects.filter(lessionexam=lessionExam)
    d = {'data': data,'class_memberships': class_memberships, 'class_membership':class_membership.class_membership, 'courses': courses, 'course': course, 'lessionExam': lessionExam, 'submitLessionExams':submitLessionExams}
    

    return render(request, 'dashboardTeacherCourseLessionExamIdView.html', d)


def ManageTeacherClassCourseLessionExamAdd(request, class_membership_id, pid, id_chuong):
    if request.method == "GET":
        user = User.objects.get(username=request.user.username)
        data = GetUser(user)
        class_membership = get_object_or_404(ClassMembership, id=class_membership_id)
        class_membershipss = Get_class_membershipss(data)
        course = Course.objects.get(id=pid)
        tags = Tag.objects.all()
        chuong = ChuongTag.objects.get(id=id_chuong)
        
        d = {'data': data, 'chuong': chuong,'class_membership': class_membership, 'class_memberships': class_membershipss, 'course': course, 'tags': tags}
        return render(request, 'dashboardTeacherClassCourseLeassonexamIdAdd.html', d)
    if request.method == "POST":
        name  = request.POST.get('name', '')
        
        content  = request.POST.get('content', '')
        timestart  = request.POST.get('timestart', '')
        timeend  = request.POST.get('timeend', '')
        course = get_object_or_404(Course, id=pid)

        chuongTag = ChuongTag.objects.get(id=id_chuong)

        
        LessionExam.objects.create(name=name, content=content, course=course, timestart=timestart, timeend=timeend, chuongTag=chuongTag)
        
        return redirect('manageTeacherClassCourse', class_membership_id, pid)
    
def ManageTeacherClassCourseLessionExamEdit(request, class_membership_id, pid, idlessionexam):
    if request.method == "GET":
        user = User.objects.get(username=request.user.username)
        data = GetUser(user)
        class_membership = get_object_or_404(ClassMembership, id=class_membership_id)
        class_membershipss = Get_class_membershipss(data)
        course = Course.objects.get(id=pid)

        lessionexam = get_object_or_404(LessionExam, id=idlessionexam)
        
        d = {'data': data, 'class_membership': class_membership, 'class_memberships': class_membershipss, 'course': course, 'lessionexam': lessionexam}
        return render(request, 'dashboardTeacherClassCourseLeassonexamIdEdit.html', d)
    if request.method == "POST":
        name  = request.POST.get('name', '')
        tag  = request.POST.get('tag', '')
        images  = request.POST.get('image', '')
        linkvideo  = request.POST.get('linkvideo', '')
        linkredirect  = request.POST.get('linkredirect', '')
        content  = request.POST.get('content', '')
        timestart  = request.POST.get('timestart', '')
        timeend  = request.POST.get('timeend', '')
        # course = get_object_or_404(Course, id=pid)

        # tagObject = get_object_or_404(Tag, id=tag)
        lessionexam = get_object_or_404(LessionExam, id=idlessionexam)

        if lessionexam:
            if name and name!= lessionexam.name:
                lessionexam.name = name
            if images and images!= lessionexam.images:
                lessionexam.images =images
            if linkvideo and linkvideo!= lessionexam.linkvideo:
                lessionexam.linkvideo = linkvideo
            if linkredirect and linkredirect!= lessionexam.linkredirect:
                lessionexam.linkredirect = linkredirect
            if content and content!= lessionexam.content:
                lessionexam.content = content
            if timestart and timestart!= lessionexam.timestart:
                lessionexam.timestart = timestart
            if timeend and timeend!= lessionexam.timeend:
                lessionexam.timeend = timeend
            lessionexam.save()

        return redirect('manageTeacherClassCourse', class_membership_id, pid)

def ManageTeacherClassCourseLessionExamDelete(request, class_membership_id, pid, idlessionexam):
    lessionexam = get_object_or_404(LessionExam, id=idlessionexam)
    lessionexam.delete()
    return redirect('manageTeacherClassCourse', class_membership_id, pid)


def ManageTeacherClassCoursetracnghiemAdd(request, class_membership_id, pid, id_chuong):
    if request.method == "GET":
        user = User.objects.get(username=request.user.username)
        data = GetUser(user)
        class_membership = get_object_or_404(ClassMembership, id=class_membership_id)
        class_membershipss = Get_class_membershipss(data)
        course = Course.objects.get(id=pid)
        tags = Tag.objects.all()
        chuong = ChuongTag.objects.get(id=id_chuong)
        
        d = {'data': data, 'chuong': chuong,'class_membership': class_membership, 'class_memberships': class_membershipss, 'course': course, 'tags': tags}
        return render(request, 'dashboardTeacherClassCourseTracNghiemIdAdd.html', d)
    if request.method == "POST":
        # Viết giúp tôi
        pass

def ManageTeacherClassCoursetracnghiemEdit(request, class_membership_id, pid, idlessionexam):
    return redirect('manageTeacherClassCourse', class_membership_id, pid)

def ManageTeacherClassCoursetracnghiemDelete(request, class_membership_id, pid, idlessionexam):
    return redirect('manageTeacherClassCourse', class_membership_id, pid)

def ManageTeacherClassCourseLessionExamGradingexam(request, class_membership_id, pid, idlessionexam):
    if request.method == "GET":
        user = User.objects.get(username=request.user.username)
        data = GetUser(user)
        class_membership = get_object_or_404(ClassMembership, id=class_membership_id)
        class_membershipss = Get_class_membershipss(data)
        course = Course.objects.get(id=pid)
        tags = Tag.objects.all()

        lessionexam = get_object_or_404(LessionExam, id=idlessionexam)
        submitLessionExams = SubmitLessionExam.objects.filter(lessionexam=lessionexam)
        
        d = {'data': data, 'class_membership': class_membership, 'class_memberships': class_membershipss, 'course': course, 'tags': tags, 'lessionexam': lessionexam, 'submitLessionExams': submitLessionExams}
        return render(request, 'manageTeacherClassCourseLessionExeamGradingexam.html', d)
    if request.method == "POST":
        user = User.objects.get(username=request.user.username)
        data = GetUser(user)
        class_membership = get_object_or_404(ClassMembership, id=class_membership_id)
        class_membershipss = Get_class_membershipss(data)
        course = Course.objects.get(id=pid)
        tags = Tag.objects.all()

        lessionexam = get_object_or_404(LessionExam, id=idlessionexam)
        submitLessionExams = SubmitLessionExam.objects.filter(lessionexam=lessionexam)

        result_name  = request.POST.get('result', '')
        description  = request.POST.get('description', '')
        id_submition  = request.POST.get('id_submition', '')
        id_user  = request.POST.get('id_user', '')
        student = StudentUser.objects.get(id=id_user)

        submitLessionExam = get_object_or_404(SubmitLessionExam, id=id_submition)


        if submitLessionExam.result:
            result = submitLessionExam.result
            if result.result != result_name:
                result.result =result_name
            if result.description != description:
                result.result =description
            result.save()
        else:
            result = Result.objects.create(result=result_name, description=description, lessionexam=lessionexam,user=student)
            submitLessionExam.result = result
            submitLessionExam.save()          

        return redirect('manageTeacherClassCourseLessionExeamGradingexam', class_membership_id, pid, idlessionexam)