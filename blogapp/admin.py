from django.contrib import admin
from blogapp.models import uploadForm

# Register your models here.
class uploadForm(admin.ModelAdmin):
    list_display=['title','description','pic']
admin.site.register(uploadForm)
#admin.site.register(postblog)
