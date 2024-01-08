from django.db import models

# Create your models here.

class Person(models.Model):
    s_opt = {
        'M': 'MALE',
        'F': 'FEMALE'
    }
    
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    date_updated = models.DateTimeField(auto_now_add=True)
    get_sex = models.CharField(max_length=6, choices=s_opt)
    def __str__(self):
        return self.fname +' '+ self.lname 
