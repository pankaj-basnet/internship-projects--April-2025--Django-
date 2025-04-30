from django.contrib import admin
from .models import Note, User


class NoteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Note, NoteAdmin)

class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)