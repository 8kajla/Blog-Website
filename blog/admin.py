from django.contrib import admin
from .models import Post,Author,Tag,Comments
# Register your models here.
class AdminPost(admin.ModelAdmin):
    list_filter = ("author","tag","date")
    list_display = ("title","date","author")
    prepopulated_fields={"slug":("title",)}

class AdminAuthor(admin.ModelAdmin):
    prepopulated_fields={"slug_author":("first_name","last_name")}

class AdminComments(admin.ModelAdmin):
    list_display = ('user_name','email','post')



admin.site.register(Post,AdminPost)
admin.site.register(Author,AdminAuthor)
admin.site.register(Tag)
admin.site.register(Comments,AdminComments)