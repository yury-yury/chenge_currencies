from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from main.models import Currency


@csrf_exempt   # Декоратор отменяющий проверку токена
def change_currencies(request, ):
    if request.method == 'GET':
        _from = request.GET.get("from", None)
        _to = request.GET.get("to", None)
        value = request.GET.get("value", 1)

        if _from is None:
            return JsonResponse({"error": 'You must specify the name of the original currency'})
        try:
            cur_from = Currency.objects.get(symbol=_from)
        except Currency.DoesNotExist:
            return JsonResponse({"error": 'The specified currency name is not in the database.'})

        if _to is None:
            return JsonResponse({"error": 'You must specify the name of the target currency'})
        try:
            cur_to = Currency.objects.get(symbol=_to)
        except Currency.DoesNotExist:
            return JsonResponse({"error": 'The specified currency name is not in the database.'})

        result: float = int(value) / cur_from.rate * cur_to.rate

    return JsonResponse({"result": result})
