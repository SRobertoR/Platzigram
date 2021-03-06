"""Posts model."""

# Django
from django.contrib import admin

# Models
from posts.models import Posts


@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""

    list_display = ('id', 'user', 'title', 'photo')
    search_fields = ('title', 'user__username', 'user__email')
    list_filter = ('created', 'modified')
