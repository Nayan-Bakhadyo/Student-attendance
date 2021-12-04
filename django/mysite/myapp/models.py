from django.db import models
from django.core.exceptions import ValidationError

class UserDetail(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=200)
    user_id = models.IntegerField('ID', null=True)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "userdetail"
  
class Detected(models.Model):
    id=models.AutoField(primary_key=True, auto_created=True)
    user_id = models.IntegerField('ID', null=True )
    date = models.DateField('Detected date')
    time = models.TimeField('Detected time')

    class Meta:
        db_table = "detected"
 

   

    