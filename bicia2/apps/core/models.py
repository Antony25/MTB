# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

EVENT_CATEGORIES = (
    ('P', 'Principiante'),
    ('I', 'Intermedia'),
    ('A', 'Avanzada'),
)

CYCLIST_CATEGORIES = (
    ('P', 'Principiante'),
    ('I', 'Intermedia'),
    ('A', 'Avanzada'),
)

SIZE_OPTIONS  = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'X Large'),
    ('XXL', 'XX Large'),
)

PACKAGE_OPTIONS  = (
    ('D', 'Entregado'),
    ('U', 'Pendiente'),
)

SUSCRIPTION_STATUS  = (
    ('A', 'Accepted'),
    ('P', 'In Process'),
)

class Event(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    cost = models.DecimalField(max_digits=4, decimal_places=3)
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    category =  models.CharField(max_length=1, choices=EVENT_CATEGORIES, default='P')


class Cyclist(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    secondlastname = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    birthday = models.DateField() 
    created = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=50)
    category = models. CharField(max_length=1, choices=CYCLIST_CATEGORIES, default='P')
    alias = models.CharField(max_length=50)
    club = models.CharField(max_length=50)
    emergency_phone = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=50)
    contact_phone = models.CharField(max_length=50)


class Suscription(models.Model):
    event = models.ForeignKey(Event)
    cyclist = models.ForeignKey(Cyclist)
    number = models.PositiveIntegerField()
    jersey = models.BooleanField(default=False)
    medal = models.BooleanField(default=False)
    ride = models.BooleanField(default=False)    
    size = models.CharField(max_length=1, choices=SIZE_OPTIONS, default='L')
    package = models.CharField(max_length=1, choices=PACKAGE_OPTIONS, default='U')
    status = models.CharField(max_length=1, choices=SUSCRIPTION_STATUS, default='U')


class Medal(models.Model):
    event = models.ForeignKey(Event)
    total = models.PositiveIntegerField(default=0)
    amount = models.PositiveIntegerField(default=0)


class Jersey(models.Model):
    event = models.ForeignKey(Event)
    total = models.PositiveIntegerField(default=0)
    amount = models.PositiveIntegerField(default=0)