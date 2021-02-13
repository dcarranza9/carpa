from django.contrib import admin
from harvests.models import Bunch, CategoryBunch

@admin.register(Bunch)
class BunchAdmin(admin.ModelAdmin):
    fields = ('category', 'weight')


@admin.register(CategoryBunch)
class CategoryBunchAdmin(admin.ModelAdmin):
    fields = ('name', )
