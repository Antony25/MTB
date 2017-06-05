# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Features(models.Model):
  event = models.ForeignKey(Events)
  jersey = models.BooleanField(default=False)
  medal = models.BooleanField(default=False)
  meal = models.BooleanField(default=False)
  transport = models.BooleanField(default=False)
  hydration = models.BooleanField(default=False)

