from django.db import models

class Register(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=32)

    #class Meta:
   	#db_table = 't_userapp'
