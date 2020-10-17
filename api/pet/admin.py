# Django:
from django.contrib import admin

# Models:
from api.pet.models import Breed, Pet, Specie

admin.site.register(Breed)
admin.site.register(Pet)
admin.site.register(Specie)
