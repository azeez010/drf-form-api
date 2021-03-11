from django.db import models

# Create your models here.
class Formdata(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    company_name = models.CharField(max_length=150)
    interested_in = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    budget = models.IntegerField()
    contact_number = models.CharField(max_length=11)
    about_project = models.TextField()
    file_upload = models.FileField(upload_to="files", blank=True)
    