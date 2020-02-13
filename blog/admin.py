from django.contrib import admin
from .models import Post
from .models import Murich



class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Murich, AuthorAdmin)
#admin.site.register(Murich)
admin.site.register(Post)
