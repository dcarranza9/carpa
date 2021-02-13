from django.contrib import admin
from harvests.models import Bunch, CategoryBunch
from main.admin import BaseModelAdmin


@admin.register(Bunch)
class BunchAdmin(admin.ModelAdmin):
    readonly_fields = BaseModelAdmin.readonly_fields
    fieldsets = (
        (None, {
            'fields': ('category', 'weight'),
        }),
        ('Audit', {
            'fields': BaseModelAdmin.readonly_fields
        })
    )


@admin.register(CategoryBunch)
class CategoryBunchAdmin(admin.ModelAdmin):
    readonly_fields = BaseModelAdmin.readonly_fields
    fieldsets = (
        (None, {
            'fields': ('name', ),
        }),
        ('Audit', {
            'fields': BaseModelAdmin.readonly_fields
        })
    )
