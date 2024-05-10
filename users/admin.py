from django.contrib import admin
from .models import User, Teachers, Groups, Courses, Rooms
# Register your models here.
admin.site.register([User, Teachers, Groups, Courses, Rooms])

