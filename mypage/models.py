from django.db import models


class Dog(models.Model):

    Breed = models.CharField(max_length=50)
    Country_of_Origin = models.CharField(max_length=50)
    Fur_Color = models.CharField(max_length=50)
    Height_inches = models.CharField(max_length=50)
    Color_of_Eyes = models.CharField(max_length=50)
    Longevity_yrs = models.CharField(max_length=50)
    Character_Traits = models.CharField(max_length=150)
    Common_Health_Problems = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='static/dog_image/',default='static/dog_image/dog_images.png')
