from django.views.generic import ListView
from django.shortcuts import render

from .models import Product
#class based view
class ProductListView(ListView):
    #traz todos os produtos do banco de dados sem filtrar nada
    queryset = Product.objects.all()
    template_name = "products/list.html"

#function based view
#def product_list_view(request):
#    queryset = Product.objects.all()
#    context = {
#        'object_list': queryset
#    }
#    return render(request, "products/list.html", context)