from django.db import models

class Record(models.Model):
    create_date = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name