"""
URL configuration for course2023 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from course.views import *
from users.views import *
from teacher.views import *
from student.views import *
from categories.views import *

from .middleware import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # users
    path('', Home, name="home"),
    path('category/(<int:category_id>)/subcategory/(<int:subcategory_id>)/', HomeSubCategory, name="homeSubCategory"),
    path('category/(<int:category_id>)/subcategory/(<int:subcategory_id>)/blog/(<int:blog_id>)/', HomeSubCategoryBlog, name="homeSubCategoryBlog"),
    path('category/(<int:category_id>)/subcategory/', HomeCategoryBlog, name="homeCategoryBlog"),



    path('login/', LoginUser, name="loginUser"),
    path('register/', Register, name="registerUser"),
    path('logout', Logout, name="logout"),

    path('manageuser/', staff_required(ManageUser), name="manageUser"),    
    path('manageuser/newuser', staff_required(NewUser), name="newUser"),
    # path('manageuser/newuser/teacher/access(<int:pid>)', staff_required(NewUserTeacherAccess), name="newUserTeacherAccess"),
    # path('manageuser/newuser/teacher/delete(<int:pid>)', staff_required(NewUserTeacherDelete), name="newUserTeacherDelete"),
    path('manageuser/newuser/student/access(<int:pid>)', staff_required(NewUserStudentAccess), name="newUserStudentAccess"),
    path('manageuser/newuser/student/delete(<int:pid>)', staff_required(NewUserStudentDelete), name="newUserStudentDelete"),

    path('manageuser/people/student', staff_required(PeopleStudent), name="peopleStudent"),
    path('manageuser/people/student/edit', staff_required(PeopleStudentEdit), name="peopleStudentEdit"),
    path('manageuser/people/teacher', staff_required(PeopleTeacher), name="peopleTeacher"),
    path('manageuser/people/teacher/edit', staff_required(PeopleTeacherEdit), name="peopleTeacherEdit"),

    path('manageuser/class/classroom', staff_required(Classroom), name="classroom"),
    path('manageuser/class/classroom/edit(<int:pid>)', staff_required(ClassroomEdit), name="classroomEdit"),
    path('manageuser/class/classroom/delete(<int:pid>)', staff_required(ClassroomDelete), name="classroomDelete"),
    path('manageuser/studentsclassroom', staff_required(StudentsInClass), name="studentsInClass"),
    path('get_user_id/', staff_required(Add_user_in_class_by_id), name='get_user_id'),
    path('manageuser/studentsclassroom/remove(<int:pid>)', staff_required(StudentsInClassRemove), name="studentsInClassRemove"),
    path('manageuser/teachersclassroom/remove(<int:pid>)', staff_required(TeachersInClassRemove), name="teachersInClassRemove"),


    # course and factory
    path('managecourse/', staff_required(ManageCourse), name="manageCourse"),
    path('managecourse/factory/', staff_required(ManageCourseFactory), name="manageCourseFactory"),
    path('managecourse/factory/edit(<int:pid>)', staff_required(ManageCourseFactoryEdit), name="manageCourseFactoryEdit"),
    path('managecourse/factory/delete(<int:pid>)', staff_required(ManageCourseFactoryDelete), name="manageCourseFactoryDelete"),
    path('managecourse/course', staff_required(ManageCourseCourse), name="manageCourseCourse"),
    path('managecourse/course/(<int:pid>)', staff_required(ManageCourseCourseDetail), name="manageCourseCourseDetail"),

    path('managecourse/course/edit(<int:pid>)', staff_required(ManageCourseCourseEdit), name="manageCourseCourseEdit"),
    path('managecourse/course/delete(<int:pid>)', staff_required(ManageCourseCourseDelete), name="manageCourseCourseDelete"),
    
    path('managecourse/tag/', staff_required(ManageTag), name="manageTag"),
    path('managecourse/tag/edit(<int:pid>)', staff_required(ManageTagEdit), name="manageTagEdit"),
    path('managecourse/tag/delete(<int:pid>)', staff_required(ManageTagDelete), name="manageTagDelete"),
    

    path('teacher/', teacher_required(ManageTeacher), name="manageTeacher"),
    path('teacher/class(<int:pid>)', teacher_required(ManageTeacherClass), name="manageTeacherClass"),
    path('teacher/class/(<int:class_membership_id>)/course(<int:pid>)', teacher_required(ManageTeacherClassCourse), name="manageTeacherClassCourse"),
    path('teacher/class/(<int:class_membership_id>)/course(<int:pid>)/adddanhmuc', teacher_required(AddDanhmuc), name="manageTeacherClassCourseAddDanhmucccc"),
    path('teacher/class/(<int:class_membership_id>)/course(<int:pid>)/updatedanhmuc(<danhmuc_id>)', teacher_required(SuaDanhmuc), name="updatedanhmuc"),
    path('teacher/class/(<int:class_membership_id>)/course(<int:pid>)/deletedanhmuc(<danhmuc_id>)', teacher_required(XoaDanhmuc), name="deletedanhmuc"),
    path('teacher/class/(<int:class_membership_id>)/course(<int:pid>)/chuong(<int:id_chuong>)/addlesson', teacher_required(ManageTeacherClassCourseLeassonAdd), name="manageTeacherClassCourseLessionAdd"),
    path('teacher/class/(<int:class_membership_id>)/course(<int:pid>)/detail(<int:idlession>)/edit', teacher_required(ManageTeacherClassCourseEdit), name="manageTeacherClassCourseLessionEdit"),
    path('teacher/class/(<int:class_membership_id>)/course(<int:pid>)/detail(<int:idlession>)/delete', teacher_required(ManageTeacherClassCourseDelete), name="manageTeacherClassCourseLessionDelete"),
    
    path('teacher/class/(<int:class_membership_id>)/course(<int:id_course>)/lession/view(<int:id_lession>)', teacher_required(ManageTeacherClassCourseLessionView), name="manageTeacherClassCourseLessionView"),
    path('teacher/class/(<int:class_membership_id>)/course(<int:id_course>)/lessionexam/view(<int:id_lession>)', teacher_required(ManageTeacherClassCourseLessionExamView), name="manageTeacherClassCourseLessionExamView"),

    path('teacher/class/(<int:class_membership_id>)/course(<int:pid>)/chuong(<int:id_chuong>)/addlessonexam', teacher_required(ManageTeacherClassCourseLessionExamAdd), name="manageTeacherClassCourseLessionExamAdd"),
    path('teacher/class/(<int:class_membership_id>)/course(<int:pid>)/detail(<int:idlessionexam>)/editexam', teacher_required(ManageTeacherClassCourseLessionExamEdit), name="manageTeacherClassCourseLessionExeamEdit"),
    path('teacher/class/(<int:class_membership_id>)/course(<int:pid>)/detail(<int:idlessionexam>)/deleteexam', teacher_required(ManageTeacherClassCourseLessionExamDelete), name="manageTeacherClassCourseLessionExeamDelete"),

    path('teacher/class/(<int:class_membership_id>)/course(<int:pid>)/chuong(<int:id_chuong>)/addtracnghiem', teacher_required(ManageTeacherClassCoursetracnghiemAdd), name="manageTeacherClassCoursetracnghiemAdd"),
    path('teacher/class/(<int:class_membership_id>)/course(<int:pid>)/detail(<int:idtracnghiem>)/editexam', teacher_required(ManageTeacherClassCoursetracnghiemEdit), name="manageTeacherClassCoursetracnghiemEdit"),
    path('teacher/class/(<int:class_membership_id>)/course(<int:pid>)/detail(<int:idtracnghiem>)/deleteexam', teacher_required(ManageTeacherClassCoursetracnghiemDelete), name="manageTeacherClassCoursetracnghiemDelete"),
    
    path('teacher/class/students(<int:pid>)', teacher_required(ManageTeacherClassStudent), name="manageTeacherClassStudent"),


    path('student/', student_required(ManageStudent), name="manageStudent"),
    path('student/course(<int:id_course>)', student_required(ManageStudentCourse), name="manageStudentCourse"),
    path('student/course(<int:id_course>)/view(<int:id_lession>)', student_required(ManageStudentCourseLession), name="manageStudentCourseLessonView"),
    path('student/course(<int:id_course>)/exam/view(<int:id_lession>)', student_required(ManageStudentCourseLessionExam), name="manageStudentCourseLessonViewExam"),
    path('student/course(<int:id_course>)/exam/view(<int:id_lession>)/delete(<int:id_submit>)', student_required(ManageStudentCourseLessionExamDeleteSubmit), name="manageStudentCourseLessionExamDeleteSubmit"),



    path('teacher/class/(<int:class_membership_id>)/course(<int:pid>)/detail(<int:idlessionexam>)/gradingexam', teacher_required(ManageTeacherClassCourseLessionExamGradingexam), name="manageTeacherClassCourseLessionExeamGradingexam"),


    path('profileuser/', ProfileUser, name="profileUser"),
    path('editrofileuser/', EditProfileUser, name="editProfileUser"),
    path('changepassword', ChangePassword, name="changePassword"),

    path('get_classmemberships/', get_classmemberships, name='get_classmemberships'),


    path('managehome/', staff_required(ManageHomePage), name="manageHomePage"),
    path('managehome/category', staff_required(ManageHomePageCategory), name="manageHomePageCategory"),
    path('managehome/category/edit/(<int:category_id>)', staff_required(ManageHomePageCategoryEdit), name="manageHomePageCategoryEdit"),
    path('managehome/category/delete/(<int:category_id>)', staff_required(ManageCategoryDelete), name="manageHomePageCategoryDelete"),
    path('managehome/category/(<int:category_id>)/subcategory', staff_required(ManageSubcategory), name="manageHomePageSubcategory"),
    path('managehome/category/(<int:category_id>)/subcategory/(<int:subcategory_id>)/edit', staff_required(ManageSubcategoryEdit), name="manageHomePageSubcategoryEdit"),
    path('managehome/category/(<int:category_id>)/subcategory/(<int:subcategory_id>)/delete', staff_required(ManageSubCategoryDelete), name="manageHomePageSubcategoryDelete"),
    path('managehome/category/(<int:category_id>)/subcategory/(<int:subcategory_id>)/blogs', staff_required(ManageBlogs), name="manageHomePagBlogs"),
    path('managehome/category/(<int:category_id>)/subcategory/blogs', staff_required(ManageBlogs), name="manageHomePagBlogsNone"),
    path('managehome/category/(<int:category_id>)/subcategory/(<int:subcategory_id>)/blogs/add', staff_required(ManageBlogsAdd), name="manageHomePagBlogsAdd"),
    path('managehome/category/(<int:category_id>)/subcategory/(<int:subcategory_id>)/blogs/edit/(<int:blog_id>)', staff_required(ManageBlogsEdit), name="manageHomePagBlogsEdit"),
    path('managehome/category/(<int:category_id>)/subcategory/(<int:subcategory_id>)/blogs/delete/(<int:blog_id>)', staff_required(ManageBlogsDelete), name="manageHomePagBlogsDelete"),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
