from typing import List

from django.db import models


class Currency(models.Model):
    """
    The Currency class inherits the Model class from the django.db module. Defines the fields of a database table
    and their properties.
    """
    symbol = models.CharField(max_length=3)
    rate = models.FloatField(null=True, blank=True)

    class Meta:
        """
        The Meta class contains the common name of the model instance in the singular and plural used
        in the administration panel.
        """
        verbose_name: str = "Rate of currency"
        verbose_name_plural: str = "Rates of currensies"
        ordering: List[str] = ["symbol", ]

    def __str__(self) -> str:
        """
        The __str__ function overrides the method of the parent class and takes no arguments except for an instance
        of its own class. When called, returns a human-readable representation of the class instance as a string.
        """
        return f"Currency {self.symbol}"
