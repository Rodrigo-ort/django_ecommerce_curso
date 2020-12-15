from django.views.generic import ListView, DetailView
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

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return(context)