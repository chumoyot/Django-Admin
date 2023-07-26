from django.contrib import admin
from .models import Course, Instructor, Lesson

class LessonInline(admin.StackedInline):
    model = Lesson 
    extra = 5

class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [LessonInline]
    
class InstructorAdmin(admin.ModelAdmin):
    fields = ['full_time', 'user']  

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)

