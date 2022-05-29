from distutils.command.upload import upload
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
    category=models.CharField(max_length=100)
    def save_category(self):
        self.save()
    def delete_category(self):
        self.save_category()
        self.delete()
    def get_all_category(self):
        self.save_category()
    @classmethod
    def update_category(cls, id, category):
        category1=cls.objects.filter(id=id).update(category=category)
        return category1

    def __str__(self):
        return self.category    

class Picture(models.Model):
    image=models.ImageField(upload_to='pictures/')
    img_url=models.URLField(null=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    location=models.ForeignKey('Location', on_delete=models.CASCADE)
    category=models.ForeignKey('Category', on_delete=models.CASCADE)
    posted_at=models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()
    def delete_image(self):
        self.save_image()
        self.delete()
    @classmethod
    def update_image(cls,id,image):
        image1=cls.objects.filter(id=id).update(image=image)
        return image1
    @classmethod
    def get_image_by_id(cls,id):
        image1=cls.objects.filter(id=id).all()
        return image1
    @classmethod
    def filter_by_location(cls, location):
        image_location = Picture.objects.filter(location__location=location).all()
        return image_location
    @classmethod
    def search_by_category(cls,search_term):
        searched_images=cls.objects.filter(category__category__icontains=search_term)
        return searched_images   

    def __str__(self):
        return self.title

    class Meta:
        ordering=['title']