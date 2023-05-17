from django.contrib import admin
from .models import DataFile
# Register your models here.
@admin.register(DataFile)
class DataFileStoreManagerAdmin(admin.ModelAdmin):
    list_display= ("filename", "files")