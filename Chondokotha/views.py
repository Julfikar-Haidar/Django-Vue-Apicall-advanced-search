from pprint import pprint

from django.shortcuts import render
from django.http import JsonResponse
from .models import Districts, Divisions, Chondokotha, Category


def index(request):
    return render(request, "base.html")


def data(request):
    context = {

        'division': list(Divisions.objects.values()),
        'category': list(Category.objects.values()),

    }
    return JsonResponse(context, safe=False)


def districts(request):
    ins = Districts.objects
    if request.GET.get('division'):
        ins = ins.filter(division=request.GET.get('division'))

    districts = ins.values()

    dis = {

        'districts': list(districts),

    }
    return JsonResponse(dis, safe=False)


def kotha(request):
    kotha = Chondokotha.objects
    if request.GET.get('category'):
        kotha = kotha.filter(category=request.GET.get('category'))

    if request.GET.get('districts'):
        kotha = kotha.filter(districts=request.GET.get('districts'))

    kotha = kotha.values('id','title','category_id','districts__division_id','districts__division__name','category__name','districts__name')

    kotha = {
        'kotha': list(kotha)
    }

    return JsonResponse(kotha, safe=False)
# Create your views here.
