from django.contrib import admin

# Register your models here.
from .models import Serial, Cast, Comment

admin.site.register(Serial)
admin.site.register(Cast)
admin.site.register(Comment)