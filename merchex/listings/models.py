from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

import textwrap

# Create your models here.
class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'



class Listing(models.Model):
    class Type(models.TextChoices):
        DISQUES = 'R'
        VETEMENTS = 'C'
        AFFICHES = 'P'
        DIVERS = 'M'

    name = models.fields.CharField(max_length=100)    
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2021)], null=True, blank=True)
    type = models.fields.CharField(choices=Type.choices, max_length=5)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        length=22
        suffix='...'
        if len(self.description) <= length:
            return f'{self.name} ({self.description})'
        else:
            lines = textwrap.wrap(self.description, length-3, break_long_words=False)
            desc = lines[0] + ("..." if len(lines)>1 else "")
            return f'{self.name} ({desc})'
            # return ' '.join(self.description[:length+1].split(' ')[0:-1]) + suffix


class ContactUsDatas(models.Model):
    name = models.fields.CharField(max_length=100)
    email = models.fields.EmailField()
    message = models.fields.CharField(max_length=1000)