from django.contrib import admin
from .models import Author,Category,Post,Comment



class CommentAdmin(admin.ModelAdmin):
    list_display = ['email','title','content']
    list_filter = ['email','title']
    search_fields = ['email','title']
    list_editable = ['title']

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment) #,CommentAdmin

