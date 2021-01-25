from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'duration',
        'participants',
        'image',
    )

    ordering = ('price',)


admin.site.register(Course, CourseAdmin)
