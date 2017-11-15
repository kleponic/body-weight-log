# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from time import timezone
from decimal import Decimal

class BodyWeightLog(models.Model):
    """
    Record body weight log
    """
    created = models.DateTimeField(auto_now_add=True, verbose_name='Waktu Dibuat')
    date = models.DateTimeField(default=timezone.now, verbose_name='Tanggal')

    max_weight = models.DecimalField(verbose_name='Berat Maksimum', max_digits=5, decimal_places=2, default=Decimal('0'))
    min_weight = models.DecimalField(verbose_name='Berat Minimum', max_digits=5, decimal_places=2, default=Decimal('0'))

    def __unicode__(self):
        return self.date.strftime("%d-%m-%Y")
