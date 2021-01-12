from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import RegexValidator
from django.utils.safestring import mark_safe


class Courses(models.Model):
    class Meta:
        verbose_name = "الحلقة"
        verbose_name_plural = ' الحلقات '

    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255, verbose_name="اسم الحلقة")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return f' {self.course_name}  '


class Centers(models.Model):
    class Meta:
        verbose_name = "مركز الحلقة"
        verbose_name_plural = ' مراكز الحلقات '

    id = models.AutoField(primary_key=True)
    center_name = models.CharField(max_length=255, verbose_name="اسم المركز")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return f' {self.center_name}  '


class Staffs(models.Model):
    class Meta:
        verbose_name = "أستاذ"
        verbose_name_plural = ' الأساتذة '

    GENDER = [
        ('1', 'طلاب'),
        ('2', ' طالبات'),
    ]

    registration_number = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=200, verbose_name="اللقب")
    firstname = models.CharField(max_length=200, verbose_name="الاسم ")
    other_name = models.CharField(max_length=200, blank=True, verbose_name="اسم الأب")
    center_id = models.ForeignKey(Centers, on_delete=models.DO_NOTHING, verbose_name="نوع الحلقة ")
    sex = models.CharField(max_length=10, choices=GENDER, default='1', verbose_name="شطر الطلاب / الطالبات")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'({self.registration_number}) {self.firstname} {self.other_name} {self.surname}  '


class Students(models.Model):
    class Meta:
        verbose_name = "الطالب"
        verbose_name_plural = ' الطلاب '

    STATUS = [
        ('active', 'نشط'),
        ('inactive', 'غير نشط')
    ]

    GENDER = [
        ('1', 'طلاب'),
        ('2', ' طالبات'),
    ]

    registration_number = models.AutoField(primary_key=True)
    current_status = models.CharField(max_length=10, choices=STATUS, default='active')
    ikama_number = models.CharField(null=True, blank=True,max_length=200, unique=True, verbose_name=" رقم الهوية / الأقامة")
    firstname = models.CharField(max_length=200, verbose_name="الاسم ")
    surname = models.CharField(max_length=200, verbose_name="اللقب")
    other_name = models.CharField(max_length=200, blank=True, verbose_name="اسم الأب")
    sex = models.CharField(max_length=10, choices=GENDER, default='1', verbose_name="شطر الطلاب / الطالبات")
    date_of_birth = models.PositiveIntegerField(null=True, blank=True, verbose_name=" العمر ")
    date_of_admission = models.DateField(default=timezone.now, verbose_name=" تاريخ الإنظمام")
    mobile_num_regex = RegexValidator(regex="^[0-9]{10,15}$", message="الرجاء ادخال رقم الجوال بالطريقة الصحيحة!")
    parent_mobile_number = models.CharField(validators=[mobile_num_regex], max_length=13, blank=True,verbose_name="جوال الأب")
    address = models.TextField(blank=True, verbose_name="العنوان ")
    others = models.TextField(blank=True, verbose_name=" معلومات اخرى")
    course_id = models.ForeignKey(Courses, null=True, blank=True, on_delete=models.DO_NOTHING,verbose_name="نوع الحلقة ")
    center_id = models.ForeignKey(Centers, null=True, blank=True, on_delete=models.DO_NOTHING, verbose_name=" المركز ")
    staff_id = models.ForeignKey(Staffs, null=True, blank=True, on_delete=models.DO_NOTHING,
                                 verbose_name=" شيخ الحلقة ")



    def __str__(self):
        return f'({self.registration_number}) {self.firstname} {self.other_name} {self.surname}  '

    # def get_absolute_url(self):
    # return reverse('student-detail', kwargs={'pk': self.pk})


class Attendance(models.Model):
    # Subject Attendance
    class Meta:
        verbose_name = " تاريخ الحلقة "
        verbose_name_plural = ' تاريخ الحلقات '

    id = models.AutoField(primary_key=True)
    attendance_date = models.DateField(verbose_name="التاريخ ")
    objects = models.Manager()

    def __str__(self):
        return f' {self.attendance_date} '


class AttendanceReport(models.Model):
    # Individual Student Attendance
    class Meta:
        verbose_name = "رصد الدرجة"
        verbose_name_plural = ' رصد الدرجات '

    STATUS = [
        ('1', 'جيد'),
        ('2', 'جيد جدا'),
        ('3', 'ممتاز'),
        ('4', 'غير حافظ'),
        ('5', 'غائب'),
    ]
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.DO_NOTHING, verbose_name="الطالب ")
    attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE, default=timezone.now, verbose_name="تاريخ الحصة ")
    status = models.CharField(max_length=10, choices=STATUS, default='1', verbose_name="الدرجة ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return f' {self.attendance_id},{self.status},{self.student_id}  '

    class StudentResult(models.Model):
        class Meta:
            verbose_name = " الدرجة "
            verbose_name_plural = ' الدرجات '

        id = models.AutoField(primary_key=True)
        student_id = models.ForeignKey(Students, on_delete=models.CASCADE, verbose_name="الطالب")
        course_id = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name="الحلقة")
        subject_exam_marks = models.FloatField(default=0)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        objects = models.Manager()