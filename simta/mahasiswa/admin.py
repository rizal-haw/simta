from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import pembimbing, Judul 
from .models import Judul 

@admin.register(pembimbing)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Judul)
class AuthorAdmin(admin.ModelAdmin):
    pass