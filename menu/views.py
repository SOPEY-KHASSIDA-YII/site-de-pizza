from django.shortcuts import render
from django.http import HttpResponse
from menu.models import Pizza

# Create your views here.

def index(request):
    # pizzas = Pizza.objects.all()
    # pizza_names_and_prix = [Pizza.nom + ' : '+ str(Pizza.prix) + "€" for Pizza in pizzas]
    # pizza_names_and_prix_str = ' , '.join(pizza_names_and_prix)
    # return HttpResponse('les pizzas : '+pizza_names_and_prix_str)
    pizzas = Pizza.objects.all().order_by('prix')
    return render(request,'menu/index.html',{'pizzas':pizzas} )