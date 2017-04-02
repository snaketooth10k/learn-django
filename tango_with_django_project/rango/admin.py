from django.contrib import admin
from rango.models import Category, Page, UserProfile

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', )
    list_filter = ('category', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {
        'slug': ('name', )
    }


admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile)
