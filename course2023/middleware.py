from django.shortcuts import redirect
from users.models import TeacherUser
from users.models import StudentUser

def staff_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('home')  # Chuyển hướng tới trang "home" nếu không phải là staff
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def teacher_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        data = ''
        try:
            data = TeacherUser.objects.get(user=request.user)
        except:
            pass
        if not data:
            return redirect('home')  # Chuyển hướng tới trang "home" nếu không phải là staff
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def student_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        data = ''
        try:
            data = StudentUser.objects.get(user=request.user)
        except:
            pass
        if not data:
            return redirect('home')  # Chuyển hướng tới trang "home" nếu không phải là staff
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def user_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        data = ''
        try:
            data = request.user
        except:
            pass
        if not data:
            return redirect('home')  # Chuyển hướng tới trang "home" nếu không phải là staff
        return view_func(request, *args, **kwargs)
    return _wrapped_view