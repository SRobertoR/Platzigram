"""Post aplication model"""

from django.apps import AppConfig


class PostsConfig(AppConfig):
    """Post aplication settings"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
    varbose_name = 'Posts'
