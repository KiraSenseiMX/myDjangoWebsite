from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

### Follow the next steps to migrate ###
# python .\manage.py makemigrations <myapp>
# python .\manage.py sqlmigrate <myapp 0001>
# python .\manage.py migrate <myapp>