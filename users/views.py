from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, Page

from django.http import Http404
import pandas as pd

from .models import *
from .helper import *
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from django.http import HttpResponseRedirect, JsonResponse

from course.models import *
from categories.models import *


# Create your views here.
def Home(request):
    user = ''
    erro = ''
    data = ''
    result = ''
    categories ='' 

    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    # SubCategory

    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
    
    # If user is teacher
    try:
        data = TeacherUser.objects.get(user=user)
        if data:
            result = 'teacher'
    except:
        pass

    try:
        data = StudentUser.objects.get(user=user)
        if data:
            result = 'student'
    except:
        pass

    news = Blogs.objects.order_by('-created_at')[:10]
    

    d = {'result': result, 'data': data, 'subcategories': subcategories, 'categories': categories, 'news': news}
    return render(request, 'homepage.html', d)

def HomeSubCategory(request,category_id, subcategory_id):
    user =''
    data = ''
    try:
        user = User.objects.get(username=request.user.username)
        data = GetUser(user)
    except:
        pass
    erro = ''
    result = ''


    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()

    category = Category.objects.get(id=category_id)
    subcategory = get_object_or_404(SubCategory, id=subcategory_id)

    blogs = Blogs.objects.filter(subcategory=subcategory).order_by('-created_at')
    paginator = Paginator(blogs, 10)  # Chia danh sách blog thành từng trang, mỗi trang có 10 blog
    page = request.GET.get('page')  # Lấy số trang hiện tại từ tham số truy vấn
    blogs_on_page = paginator.get_page(page)  # Lấy danh sách blog cho trang hiện tại


    


    news = Blogs.objects.order_by('-created_at')[:10]
    d = {
        'result': result,
        'news': news,
        'data': data,
        'subcategories': subcategories,
        'category': category,
        'categories': categories,
        'subcategory': subcategory,
        'blogs': blogs_on_page
    }
    return render(request, 'homepageBlog.html', d)

def HomeSubCategoryBlog(request,category_id, subcategory_id, blog_id):
    user =''
    data = ''
    try:
        user = User.objects.get(username=request.user.username)
        data = GetUser(user)
    except:
        pass
    erro = ''
    result = ''


    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()

    category = Category.objects.get(id=category_id)
    subcategory = get_object_or_404(SubCategory, id=subcategory_id)
    blogs = Blogs.objects.filter(subcategory=subcategory)
    blog = Blogs.objects.get(id=blog_id)
    news = Blogs.objects.order_by('-created_at')[:10]
    d = {'result': result, 'news': news, 'data': data, 'subcategories': subcategories, 'category': category, 'categories': categories, 'blogs': blogs, 'subcategory': subcategory, 'blog': blog}
    return render(request, 'homepageBlogView.html', d)

def HomeCategoryBlog(request, category_id):
    user =''
    data = ''
    try:
        user = User.objects.get(username=request.user.username)
        data = GetUser(user)
    except:
        pass
    erro = ''
    result = ''


    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()

    category = Category.objects.get(id=category_id)
    subcategory = SubCategory.objects.filter(category=category).first()
    
    blogs = Blogs.objects.filter(subcategory=subcategory).order_by('-created_at')
    paginator = Paginator(blogs, 10)  # Chia danh sách blog thành từng trang, mỗi trang có 10 blog
    page = request.GET.get('page')  # Lấy số trang hiện tại từ tham số truy vấn
    blogs_on_page = paginator.get_page(page)  # Lấy danh sách blog cho trang hiện tại

    news = Blogs.objects.order_by('-created_at')[:10]
    d = {
        'result': result, 
        'news': news, 
        'data': data, 
        'subcategories': subcategories, 
        'category': category, 
        'categories': categories, 
        'blogs': blogs_on_page,
        'subcategory': subcategory
    }
    return render(request, 'homepageBlog.html', d)

def LoginUser(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    news = Blogs.objects.order_by('-created_at')[:10]
    if request.method == "GET":
        d = {'subcategories': subcategories, 'categories': categories, 'news': news}
        return render(request, 'login.html', d)
    if request.method == "POST":   
        result = ''
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            result = CheckRole(user)
            if (result=="notrole"):
                d = {'result': result, 'subcategories': subcategories, 'categories': categories, 'news': news}
                return render(request, 'login.html', d)

            data = GetDataUser(user)
            if (data.isActive == True):
                login(request, user)
                d = {'result': result, 'subcategories': subcategories, 'categories': categories, 'news': news, 'isLogin': True}
                return redirect('home')
            else:
                result = 'notactive'
                d = {'result': result, 'subcategories': subcategories, 'categories': categories, 'news': news}
                return render(request, 'login.html',d)
        else:
            result = 'not'
            d = {'result': result, 'subcategories': subcategories, 'categories': categories, 'news': news}
            return render(request, 'login.html',d)
  

def Register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']

        email = request.POST['email']

        username = request.POST['username']
        password = request.POST['password']

        contact = request.POST['contact']
        address = request.POST['address']
        dob = request.POST['dob']

        reg = request.POST['reg']
        image = request.FILES['image']

        user = User.objects.create_user(
            first_name=first_name, last_name=last_name, email=email, username=username, password=password)

        if reg == "teacher":
            TeacherUser.objects.create(
                user=user, contact=contact, address=address, dob=dob, image=image)
        else:
            StudentUser.objects.create(
                user=user, contact=contact, address=address, dob=dob, image=image)
        d = {'result': 'register'}
        return redirect('loginUser')

def Logout(request):
    logout(request)
    return redirect('home')



def ManageUser(request):
    user = User.objects.get(username=request.user.username)
    data = GetUser(user)
    count_inactive_users = Count_inactive_users()
    count_teacher_users = Count_teacher_users()
    count_student_users = Count_student_users()
    count_class_memberships = Count_class_memberships()
    d = {'data': data, 'count_inactive_users': count_inactive_users, 'count_teacher_users': count_teacher_users, 'count_student_users': count_student_users, 'count_class_memberships': count_class_memberships}
    return render(request, 'dashboardUser.html', d)

def NewUser(request):
    import pandas as pd

def NewUser(request):
    user = User.objects.get(username=request.user.username)    
    data = GetUser(user)
    get_inactive_students = Get_inactive_students()

    if request.method == 'POST':
        # Kiểm tra xem tệp Excel đã được tải lên
        if 'excel_file' in request.FILES:
            excel_file = request.FILES['excel_file']

            # Kiểm tra xem định dạng tệp có hợp lệ (ví dụ: .xlsx)
            if excel_file.name.endswith('.xlsx'):
                # Đọc dữ liệu từ tệp Excel bằng pandas
                df = pd.read_excel(excel_file)

                # Lặp qua các dòng trong DataFrame và thêm vào cơ sở dữ liệu
                for index, row in df.iterrows():
                    # Tạo User
                    user_data = {
                        'username': row['username'],
                        'password': row['password'],  # Cần xử lý mật khẩu đúng cách
                        'email': row['email'],
                    }
                    user = User.objects.create_user(**user_data)

                    # Tạo StudentUser và liên kết với User
                    student_data = {
                        'user': user,
                        'address': row['address'],
                        'contact': row['contact'],
                        'is_student': False,
                    }
                    StudentUser.objects.create(**student_data)
        return redirect('newUser')

    d = {'data': data, 'get_inactive_students': get_inactive_students}
    return render(request, 'newUser.html', d)


# Chuyển isActive của tài khoản thành true
def NewUserTeacherAccess(request, pid):
    # Lấy thông tin giáo viên dựa trên pid
    teacher = get_object_or_404(TeacherUser, id=pid)
    
    # Kích hoạt tài khoản giáo viên bằng cách đặt isActive=True
    teacher.isActive = True
    teacher.save()
    return redirect('newUser')

# Xóa tài khoản Teacher và user
def NewUserTeacherDelete(request, pid):
    # Lấy thông tin giáo viên dựa trên pid
    teacher = get_object_or_404(TeacherUser, id=pid)

    # Lấy user tương ứng và xóa tài khoản user
    user = teacher.user
    user.delete()

    # Xóa tài khoản giáo viên
    teacher.delete()
    return redirect('newUser')

# Chuyển isActive của tài khoản thành true
def NewUserStudentAccess(request, pid):
    # Lấy thông tin học sinh dựa trên pid
    student = get_object_or_404(StudentUser, id=pid)
    
    # Kích hoạt tài khoản học sinh bằng cách đặt isActive=True
    student.isActive = True
    student.is_student = True
    student.save()
    return redirect('newUser')

# Xóa tài khoản Student và user
def NewUserStudentDelete(request, pid):
    # Lấy thông tin học sinh dựa trên pid
    student = get_object_or_404(StudentUser, id=pid)

    # Lấy user tương ứng và xóa tài khoản user
    user = student.user
    user.delete()

    # Xóa tài khoản học sinh
    student.delete()
    return redirect('newUser')

def PeopleStudent(request):
    user = User.objects.get(username=request.user.username)
    
    data = GetUser(user)    
    get_active_students = Get_active_students()
    d = {'data': data, 'get_active_students': get_active_students}
    return render(request, 'peopleStudentUser.html', d)

def PeopleTeacher(request):
    user = User.objects.get(username=request.user.username)
    
    data = GetUser(user)
    get_active_teachers = Get_active_teachers()
    d = {'data': data, 'get_active_teachers': get_active_teachers}
    return render(request, 'peopleTeacherUser.html', d)


def PeopleStudentEdit(request):
    return HttpResponseRedirect('/admin/users/studentuser/')

def PeopleTeacherEdit(request):
    return HttpResponseRedirect('/admin/users/teacheruser/')


def Classroom(request):
    if request.method == "GET":
        user = User.objects.get(username=request.user.username)
        
        data = GetUser(user)
        factories = Factory.objects.all()
        
        classrooms = ClassMembership.objects.all()
        d = {'data': data, 'classrooms': classrooms, 'factories': factories}
        return render(request, 'classroomView.html', d)
    if request.method == "POST":
        classroom = request.POST['classroom']
        factory_id = request.POST['factory']
        factory = Factory.objects.get(id=factory_id)
        if (classroom):
            ClassMembership.objects.create(name=classroom, factory=factory)
            return redirect('classroom')
        return redirect('classroom')

def ClassroomEdit(request, pid):
    user = User.objects.get(username=request.user.username)

    classroom = get_object_or_404(ClassMembership, id=pid)
    if request.method == "GET":
        data = GetUser(user)

        d = {'data': data, 'classroom': classroom}
        return render(request, 'classroomEdit.html', d)
    if request.method == "POST":
        new_classroom_name  = request.POST['classroom']
        # Update the existing classroom object
        classroom.name = new_classroom_name
        classroom.save()  # Save the changes to the database

        return redirect('classroom')  # Redirect to the 'classroom' page after the update

def ClassroomDelete(request, pid):    
    classroom = get_object_or_404(ClassMembership, id=pid)

    classroom.delete()
    return redirect('classroom')

def StudentsInClass(request):
    user = User.objects.get(username=request.user.username)
    data = GetUser(user)

    selected_class_id = request.GET.get('classroom')
    selected_factory_id = request.GET.get('factory')
    student_memberships = ''
    teacher_memberships = ''
    students = ''
    teachers = ''
    factories = Factory.objects.all()
    factory_select =''

    if selected_class_id:
        classroom = get_object_or_404(ClassMembership, id=selected_class_id)
        if selected_factory_id:
            factory_select = get_object_or_404(Factory, id=selected_factory_id)
        student_memberships = MembershipStudentUser.objects.filter(class_membership=classroom)
        teacher_memberships = MembershipTeacherUser.objects.filter(class_membership=classroom)

        students = [membership.student for membership in student_memberships]
        teachers = [membership.teacher for membership in teacher_memberships]
    else:
        classroom = None
        students = []
        teachers = []

    classrooms = ClassMembership.objects.all()

    return render(request, 'studentsInClassView.html', {
        'data': data,
        'classroom': classroom,
        'factory_select': factory_select,
        'students': students,
        'teachers': teachers,
        'classrooms': classrooms,
        'student_memberships': student_memberships,
        'teacher_memberships': teacher_memberships,
        'factories': factories
    })

def get_classmemberships(request):
    factory_id = request.GET.get('factory_id')
    
    # Fetch ClassMemberships associated with the selected Factory
    classmemberships = ClassMembership.objects.filter(factory_id=factory_id).values('id', 'name')
    
    return JsonResponse({'classmemberships': list(classmemberships)})

def Add_user_in_class_by_id(request):
    user = User.objects.get(username=request.user.username)
    if (user.is_staff==False):
        return redirect('home')
    if request.method == 'POST':
        result=''
        user_type = request.POST.get('user_type')  # Loại người dùng: 'teacher' hoặc 'student'
        if not user_type:
            result += 'user_type not exits | '
        email = request.POST.get('email')  # Địa chỉ email của người dùng cần tìm
        if not email:
            result += 'email not exits | '
        classroom_id = request.POST.get('classroom_id')
        if not classroom_id:
            result += 'classroom_id not exits'
        newuser=''
        if user_type == 'teacher':
            newuser = TeacherUser.objects.filter(user__email=email).first()
        elif user_type == 'student':
            newuser = StudentUser.objects.filter(user__email=email).first()
        if not newuser:
            result += 'email not exits | '
        
        if user_type and newuser and classroom_id:
            UserInClassAddById(user_type, newuser.id, classroom_id)                
            return JsonResponse({'user_id': newuser.id})
    
    return JsonResponse({'erro': result})


def StudentsInClassRemove(request, pid):
    MembershipStudentUser.objects.filter(id=pid).delete()
    return redirect('studentsInClass')

def TeachersInClassRemove(request, pid):
    MembershipTeacherUser.objects.filter(id=pid).delete()
    return redirect('studentsInClass')



def ProfileUser(request):
    user = ''
    erro = ''
    data = ''
    result = ''

    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
    
    # If user is teacher
    try:
        data = TeacherUser.objects.get(user=user)
        if data:
            result = 'teacher'
    except:
        pass

    try:
        data = StudentUser.objects.get(user=user)
        if data:
            result = 'student'
    except:
        pass

    d = {'result': result, 'data': data}
    return render(request, 'profileUser.html', d)


def EditProfileUser(request):
    user = ''
    erro = ''
    data = ''
    result = ''

    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
    
    # If user is teacher
    try:
        data = TeacherUser.objects.get(user=user)
        if data:
            result = 'teacher'
    except:
        pass

    try:
        data = StudentUser.objects.get(user=user)
        if data:
            result = 'student'
    except:
        pass

    d = {'result': result, 'data': data}
    if request.method == "GET":
        return render(request, 'editProfile.html', d)
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']

        contact = request.POST['contact']
        address = request.POST['address']

        try:
            data.image = request.FILES['image']
            data.save()
        except:
            pass
        user.first_name = first_name
        user.last_name = last_name
        data.address = address
        data.contact = contact

        user.save()
        data.save()

        d = {'result': "editprofile", 'data': data}
        return render(request, 'profileUser.html', d)

def ChangePassword(request):
    user = ''
    erro = ''
    data = ''
    result = ''

    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
    
    # If user is teacher
    try:
        data = TeacherUser.objects.get(user=user)
        if data:
            result = 'teacher'
    except:
        pass

    try:
        data = StudentUser.objects.get(user=user)
        if data:
            result = 'student'
    except:
        pass

    d = {'result': result, 'data': data}
    if request.method == "GET":
        return render(request, 'editPassword.html', d)
    if request.method == "POST":
        password_current = request.POST['pw1']
        pw2 = request.POST['pw2']
        pw3 = request.POST['pw3']
        user = authenticate(username=user.username, password=password_current)
        if user and pw2 == pw3:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(pw2)
            u.save()
            d = {'result': "changepassword", 'data': data}
            return redirect('loginUser')
        else:
            d = {'result': "passnot", 'data': data}
            return render(request, 'editPassword.html', d)