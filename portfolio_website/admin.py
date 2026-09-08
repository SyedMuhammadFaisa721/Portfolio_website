from django.contrib import admin
from .models import skill, projects, contact , experience , projectimage

admin.site.register(skill)
admin.site.register(projects)
admin.site.register(contact)
admin.site.register(experience)
admin.site.register(projectimage)

# Register your models here.
