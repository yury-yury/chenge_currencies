from django.urls import path

from main.views import change_currencies

urlpatterns = [
    path("rates", change_currencies,)
]
