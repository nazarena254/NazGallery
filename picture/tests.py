from django.test import TestCase
from models import Category, Location, Picture

# Create your tests here.
class LocationTestClass(TestCase):
    #set up method
    def setUp(self):
        self.kenya=Location(location='Kenya')
    # To tear down instance
    def tearDown(self):
        Location.objects.all().delete()
    # Testing_instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kenya,Location))
    # Testing Save Method
    def test_save_method(self):
        self.kenya.save_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)>0)
    # Test Delete Method
    def test_delete_method(self):
        self.kenya.delete_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)==0)
    #Test get all method
    def test_get_all(self):
        self.kenya.get_all()
        locations=Location.objects.all()
        self.assertTrue(len(locations)==1)
    #Test update location method
    def test_update_location(self):
        self.kenya.save_location()
        self.kenya.update_location(self.kenya.id,'Rwanda')
        rwanda=Location.objects.get(location='Rwanda')
        self.assertEqual(rwanda.location,'Rwanda')

class CategoryTestClass(TestCase):
    #set up method
    def setUp(self):
        self.food=Category(category='Food')
    # To tear down instance
    def tearDown(self):
        Category.objects.all().delete()
    # Testing_instance
    def test_instance(self):
        self.assertTrue(isinstance(self.food,Category))
    # Testing Save Method
    def test_save_method(self):
        self.food.save_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)
    #Test delete category method
    def test_delete_method(self):
        self.food.delete_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)==0)
    # Test get all categories method
    def test_get_all(self):
        self.food.get_all_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)==1)    
    #Test update category
    def test_update_category(self):
        self.food.save_category()
        self.food.update_category(self.food.id,'Fashion')
        fashion=Category.objects.get(category='Fashion')
        self.assertEqual(fashion.category,'Fashion')

class PictureTestClass(TestCase):
    def setUp(self):
        self.kenya=Location(location='Kenya')
        self.kenya.save_location()
        self.food=Category(category='Food')
        self.food.save_category()
        self.new_picture=Picture(title='WaterFalls',description='A waterfall',location=self.kenya,category=self.food)
        self.new_picture.save()
    def tearDown(self):
        Picture.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
    def test_picture_instance(self):
        self.assertTrue(isinstance(self.new_picture,Picture))
    def test_save_picture(self):
        self.new_picture.save_image()
        images=Picture.objects.all()
        self.assertTrue(len(images)>0)
    def test_delete_picture(self):
        self.new_picture.delete_image()
        images=Picture.objects.all()
        self.assertTrue(len(images)==0)
    def test_update_image(self):
        self.new_picture.save_image()
        self.new_picture.update_image(self.new_picture.id,image='media/test.png')
        image_new=Picture.objects.get(image='media/test.png')
        self.assertEqual(image_new.image,'media/test.png')
    def test_get_image_by_id(self):
        self.new_picture.save_image()
        image_found=self.new_picture.get_image_by_id(self.new_picture.id)
        self.assertTrue(len(image_found)>0)
    def test_filter_by_location(self):
        self.new_picture.save_image()
        found_images = self.new_picture.filter_by_location(location='Kenya')
        self.assertTrue(len(found_images) == 1)
    def test_search_image(self):
        self.new_picture.save_image()
        searched_image=self.new_picture.search_by_category(search_term='food')
        self.assertTrue(len(searched_image)==1)                