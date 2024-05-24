from django.contrib import admin

from core import models


class WorkerInline(admin.TabularInline):
    model = models.Worker
    extra = 1


@admin.register(models.Department)
class Department(admin.ModelAdmin):
    list_filter = ['name', ]
    inlines = [WorkerInline, ]

    def has_add_permission(self, request):
        return False


@admin.register(models.Worker)
class Worker(admin.ModelAdmin):
    list_filter = ['last_name', 'gender', 'dc']

    def has_add_permission(self, request):
        return False
