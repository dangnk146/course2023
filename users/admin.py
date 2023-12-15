from django.contrib import admin
from .models import *

from course.models import *

# Register your models here.
admin.site.register(ClassMembership)

admin.site.register(TeacherUser)
admin.site.register(StudentUser)
admin.site.register(MembershipStudentUser)
admin.site.register(MembershipTeacherUser)
