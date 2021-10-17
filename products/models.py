from django.db import models

# Create your models here

class Category(models.Model):
    name = models.CharField(max_length=20)


    class Meta:
        db_table = 'categories'

class Nutrition(models.Model):
    one_serving_kcal = models.IntegerField(default=0)
    sodium_mg = models.IntegerField(default=0)
    saturated_fat_g = models.IntegerField(default=0)
    sugars_g = models.IntegerField(default=0)
    protein_g = models.IntegerField(default=0)
    caffeine_mg = models.IntegerField(default=0)

    class Meta:
        db_table = 'nutritions'

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    korean_name = models.CharField(max_length=30)
    english_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    nutrition = models.ForeignKey(Nutrition, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

class Image(models.Model):
    image_url = models.CharField(max_length=500)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

class Allergy(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'allergy'

class Allergy_product(models.Model):
    allergy = models.ForeignKey(Allergy, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergy_products'
    
    

