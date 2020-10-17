from django.db import models


class Specie(models.Model):
    species = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.species


class Breed(models.Model):
    breed = models.CharField(max_length=255)
    description = models.TextField()
    species = models.ForeignKey(Specie, on_delete=models.CASCADE)

    def __str__(self):
        return self.breed


class Pet(models.Model):
    GENDER_CHOICES = [
        ("M", "MALE"),
        ("F", "FEMALE")
    ]

    photo = models.ImageField("Uploaded image")
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    weight = models.FloatField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " - " + self.breed.breed
