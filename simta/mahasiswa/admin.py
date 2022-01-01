from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Pembimbing, Judul 
from .models import Judul 

@admin.register(Pembimbing)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Judul)
class AuthorAdmin(admin.ModelAdmin):
    pass