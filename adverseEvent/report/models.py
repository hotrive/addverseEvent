from django.db import models

# Create your models here.
# 科室表
class Department(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


# 用户表
class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=100)
    register_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username


# 医生表
class Doctor(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    phone = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=100)
    register_time = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name


# 患者表
class Patient(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    phone = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=100)
    register_time = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name


# 不良事件类型表
class BadEventType(models.Model):
    type_name = models.CharField(max_length=20)
    type_description = models.TextField()

    def __str__(self):
        return self.type_name


# 不良事件表
class BadEvent(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    bad_event_type = models.ForeignKey(BadEventType, on_delete=models.CASCADE, default=None, null=True)
    event_time = models.DateTimeField(auto_now_add=True)
    event_description = models.TextField()
    event_status = models.CharField(max_length=20)

    def __str__(self):
        return self.event_description

# 不良事件处理表
class BadEventHandle(models.Model):
    bad_event = models.ForeignKey(BadEvent, on_delete=models.CASCADE)
    handle_time = models.DateTimeField(auto_now_add=True)
    handle_description = models.TextField()
    handle_status = models.CharField(max_length=20)


    def __str__(self):
        return self.handle_description
