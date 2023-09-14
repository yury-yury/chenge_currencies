from django.db import models


class Currency(models.Model):
    symbol = models.CharField(max_length=3)
    rate = models.FloatField()

    class Meta:
        verbose_name = "Курс валюты"
        verbose_name_plural = "Курсы валют"
        ordering = ["symbol", ]

    def __str__(self):
        return self.symbol
