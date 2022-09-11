from django.contrib import admin
from blog.models import Post,Category
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('author','title','status','category','created_date','updated_date')

admin.site.register(Post,PostAdmin)
admin.site.register(Category)