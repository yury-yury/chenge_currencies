from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from main.models import Currency


@csrf_exempt
def change_currencies(request, ):
    """
    The change_currencies function is an FBV for the "/api/rates" endpoint,
    accepting a request made using the GET method. Takes a request object as a parameter.
    Contains all the necessary logic for validating the received data and generating a response.
    Returns a response in JSON format.
    """
    if request.method == 'GET':
        _from = request.GET.get("from", None)
        _to = request.GET.get("to", None)
        value = request.GET.get("value", 1)

        if _from is None or _to is None:
            return JsonResponse({"error": 'You must specify the names of the original and target currencies'})

        try:
            cur_from = Currency.objects.get(symbol=_from)
            cur_to = Currency.objects.get(symbol=_to)
        except Currency.DoesNotExist:
            return JsonResponse({"error": 'The specified currency name is not in the database.'})

        result: float = int(value) / cur_from.rate * cur_to.rate

    return JsonResponse({"result": result})
