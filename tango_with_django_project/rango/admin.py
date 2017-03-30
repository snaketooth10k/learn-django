from django.contrib import admin
from rango.models import Category, Page

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', )
    list_filter = ('category', )

admin.site.register(Page, PageAdmin)
admin.site.register(Category)
