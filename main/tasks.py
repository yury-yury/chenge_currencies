import os
from typing import Dict, Any
from celery import shared_task
import requests

from main.models import Currency


@shared_task
def update_database() -> None:
    """
    The update_database function is a periodic task. Does not accept arguments.
    When called, it requests data on current exchange rates from the API of the site https://openexchangerates.org.
    Creates or updates instances of the Currency model according to the received data.
    """
    response: Dict[str, Any] = requests.get(
        f"https://openexchangerates.org/api/latest.json?app_id={os.getenv('APP_ID')}").json()['rates']

    for symbol, rate in response.items():
        instance, _ = Currency.objects.get_or_create(symbol=symbol)
        instance.rate = rate
        instance.save()
