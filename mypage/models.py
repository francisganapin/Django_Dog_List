from django.db import models


class DogAdoption(models.Model):



class Dog(models.Model):
    breed = models.CharField(max_length=50)
    country_of_origin = models.CharField(max_length=50)
    fur_color = models.CharField(max_length=50)
    height_inches = models.CharField(max_length=50)
    color_of_eyes = models.CharField(max_length=50)
    longevity_yrs = models.CharField(max_length=50)
    image = models.ImageField(upload_to='dog_image')

    def __str__(self):
        return self.breed

class CharacterTrait(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name="character_traits")
    trait = models.CharField(max_length=100)

    def __str__(self):
        return self.trait

class HealthProblem(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name="health_problems")
    health_problem = models.TextField()

    def __str__(self):
        return self.health_problem
