from django.contrib import admin
from .models import User, Doctor, Department, Patient, BadEvent, BadEventType, BadEventHandle

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email', 'phone', 'address', 'register_time')
    list_filter = ('register_time',)
    

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'age', 'phone', 'address', 'register_time')
    list_filter = ('register_time', 'gender')
    


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'age', 'phone', 'address','register_time', 'doctor')
    list_filter = ('register_time', 'doctor')
    


@admin.register(BadEvent)
class BadEventAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'bad_event_type', 'event_time', 'event_description', 'event_status')
    list_filter = ('event_time', 'bad_event_type')
    


@admin.register(BadEventType)
class BadEventTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name', 'type_description')
    search_fields = ('type_name',)
    


@admin.register(BadEventHandle)
class BadEventHandleAdmin(admin.ModelAdmin):
    list_display = ('bad_event', 'handle_time', 'handle_description', 'handle_status')
    list_filter = ('handle_time',)
    ordering = ('handle_time',)