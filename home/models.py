from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hotel_Room_Application_Record(models.Model):
    #Room number is alphanumeric
    Room_number = models.CharField(max_length=5)
    Amount_paid_in_Naira = models.DecimalField(max_digits=10000000, decimal_places=2)
    Occupant_Name = models.CharField(max_length=1000)
    Occupant_email = models.EmailField()
    Occupant_occupation = models.CharField(max_length=10000)
    Number_of_night = models.IntegerField()
    Start_date = models.DateField()
    End_date = models.DateField()
    Registered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Occupant_Name + " - " + self.Room_number

    #def snippet(self):
    #   return self.Occupant_Name[:1] + "..."