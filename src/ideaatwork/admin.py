from django.contrib import admin

from ideaatwork.models import Idea

@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    fields = ["title", "body", "suggested_by"]
    readonly_fields = ["published_on"]