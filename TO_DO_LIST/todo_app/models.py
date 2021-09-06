from django.db import models

# Create your models here.
class todo_List(models.Model):
    desc = models.TextField(max_length=100)