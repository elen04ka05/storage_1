from django.contrib import admin
from .models import Task, Sign, Snippet, Input


admin.site.register(Task)
admin.site.register(Sign)
admin.site.register(Snippet)
admin.site.register(Input)