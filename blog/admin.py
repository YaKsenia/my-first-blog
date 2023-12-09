from django.contrib import admin
from .models import Post
from .models import Murich
from .models import HuckYou
from .models import Images

class AuthorAdmin(admin.ModelAdmin):
    change_form_template = 'blog/admin/change_form.html'

admin.site.register(Murich, AuthorAdmin)
admin.site.register(Post)
admin.site.register(HuckYou)
admin.site.register(Images)
