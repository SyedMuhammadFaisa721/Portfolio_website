from django.db import models

class skill(models.Model):
    skill_name = models.CharField(max_length = 200 , primary_key = True)
    skill_description = models.TextField()
    skill_logo  = models.CharField(max_length = 50)

    def __str__(self):
        return self.skill_name

class projects(models.Model):
    project_serial_number = models.IntegerField(primary_key = True )
    project_name = models.CharField(max_length = 200)
    project_description = models.TextField()
    project_language = models.CharField(max_length = 300)

    def __str__(self):
        return self.project_name

class contact(models.Model):
    contact_name = models.CharField(max_length = 200)
    contact_email = models.EmailField()
    contact_subject = models.CharField(max_length = 200)
    project_type = models.CharField(max_length = 400)
    contact_message = models.TextField()

    def __str__(self):
        return self.contact_email

class experience(models.Model):
    experience_title = models.CharField(max_length = 200 , primary_key = True)
    experience_description = models.TextField()
    experience_duration = models.CharField(max_length = 200)
    experience_company = models.CharField(max_length = 200)

    def __str__(self):
        return self.experience_title
# Create your models here.
