from django.db import models

class ordem(models.Model):
    numero_id = models.AutoField(primary_key = True)
    Os_numero = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')

class Person(models.Model):	
    name = models.CharField(max_length=30)
    numero = models.CharField(max_length=30)