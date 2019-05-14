from django.shortcuts import render

from django.http import JsonResponse
from api.models import TaskList


def category_list(request):
    categories = TaskList.objects.all()
    json_categories = [c.to_json() for c in categories]
    return JsonResponse(json_categories, safe=False)


def category_detail(request, pk):
    try:
        category = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(category.to_json())


def category_product(request, pk):
    try:
        category = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    products = category.task_set.all()
    json_products = [p.to_json() for p in products]
    return JsonResponse(json_products, safe=False)