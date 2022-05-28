from django.db import models

# Create your models here.
class Location(models.Model):
    location=models.CharField(max_length=150)
    def save_location(self):
        self.save()
    def delete_location(self):
        self.save_location()
        self.delete()
    def get_all(self):
         self.save_location()
    @classmethod
    def update_location(cls, id, location):
        location1=cls.objects.filter(id=id).update(location=location)
        return location1 

    def __str__(self):
        return self.location             

class Category(models.Model):
    pass
