from django.contrib import admin
from .models import Project, Category, Contact, Slider, BlogPost, Transformation, Service

admin.site.register(Transformation)
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(Slider)
admin.site.register(BlogPost)
admin.site.register(Service)