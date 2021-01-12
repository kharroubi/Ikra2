from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.fields import Field

from django.contrib.admin import site
#import adminactions.actions as actions

# register all adminactions
#actions.add_to_site(site)

admin.site.site_header = 'منصـة جمعية إقرأ'
admin.site.site_title = "الحـلقات القرآنية بالـخـرمــة"
admin.site.index_title = "إدارة منصة الجمعية بالـخـرمــة"


class CoursesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Courses


admin.site.register(Courses, CoursesAdmin)


class StaffsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Staffs


admin.site.register(Staffs, StaffsAdmin)


class CentersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Centers


admin.site.register(Centers, CentersAdmin)


class StudentsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Students

    list_display = (
     'firstname', 'other_name', 'surname', 'center_id', 'sex', 'course_id', 'staff_id',)
    search_fields = ['ikama_number', 'firstname', ]
    list_filter = ['center_id', 'sex', 'course_id', 'staff_id']
    list_per_page = 30
    list_display_links = ["firstname", ]
    # readonly_fields = ('staff_id',)


admin.site.register(Students, StudentsAdmin)

admin.site.register(Attendance)


class AttendanceReportAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = AttendanceReport
    list_display = ('attendance_id', 'student_id', 'status')
    search_fields = ['student_id', 'attendance_id', ]
    list_filter = ['status', 'attendance_id', ]
    list_per_page = 30


admin.site.register(AttendanceReport, AttendanceReportAdmin)