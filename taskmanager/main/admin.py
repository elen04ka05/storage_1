from django.contrib import admin
from .models import Task, Sign, Snippet


admin.site.register(Task)
admin.site.register(Sign)
admin.site.register(Snippet)