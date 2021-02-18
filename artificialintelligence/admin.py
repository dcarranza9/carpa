from artificialintelligence.models import ProcessedImage
from django.contrib import admin
from main.admin import BaseModelAdmin


@admin.register(ProcessedImage)
class ProcessedImageAdmin(admin.ModelAdmin):
    readonly_fields = BaseModelAdmin.readonly_fields
    fieldsets = (
        (None, {
            'fields': ('name', 'image', 'bunches'),
        }),
        ('Audit', {
            'fields': BaseModelAdmin.readonly_fields
        })
    )
    list_display = ('id', 'name', 'creation_date', 'update_date')
    list_filter = ('creation_date',)
