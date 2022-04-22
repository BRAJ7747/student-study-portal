from django.contrib import admin
from .models import Notes, HomeWork, Todo

# Register your models here.
@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    display_list=['id','user','title','description']


@admin.register(HomeWork)
class HomeWorkAdmin(admin.ModelAdmin):
    display_list=['id','user','subject','title',"description", 'due','is_finished']
    
    
@admin.register(Todo) 
class TodoAdmin(admin.ModelAdmin):
    display_list=['id', 'user', 'title', 'is_finished']   