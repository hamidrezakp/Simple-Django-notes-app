from django.contrib import admin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    readonly_fields= ['created_at', 'updated_at', 'author']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Note, NoteAdmin)
