from django.contrib import admin
from app.models import Category, Page
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

    def __str__(self):
        return self.list_display


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)




