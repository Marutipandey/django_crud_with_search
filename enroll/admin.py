from django.contrib import admin
from.models import Student
# Register your models here.
@admin.register(Student)
class stuAdmin(admin.ModelAdmin):
    list_display = ['stuname','stuemail','stuage','stuphoto','stubranch','stucontact']
