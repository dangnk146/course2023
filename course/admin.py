from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Factory)
admin.site.register(Course)


admin.site.register(Tag)

admin.site.register(Lession)
admin.site.register(LessionExam)

admin.site.register(TagLessionCourse)
admin.site.register(TagLessionExameCourse)

admin.site.register(Result)
admin.site.register(SubmitLessionExam)


