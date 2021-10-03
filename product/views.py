from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from rest_framework import generics
from rest_framework import mixins

from fcuser.decorators import admin_required
from .models import Product
from .forms import RegisterForm
from .serializers import ProductSerializer
from order.forms import RegisterForm as OrderForm

# Create your views here.

class ProductListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProductDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'
   
    paginate_by = 3
    # ordering='register_date'
    # page_kwarg='page'
<<<<<<< HEAD

=======
>>>>>>> 7d33ea541317b3b907e7618106820dc8e91fcd84

############# 추가1
    def get_queryset(self):     
        # print(f'self.request.GET is {self.request.GET.get(key="s")}')
        search_word=self.request.GET.get(key='s')
        if search_word:
            return Product.objects.filter(name__contains=search_word).order_by('-register_date')
        else:
            return Product.objects.all().order_by('-register_date')
<<<<<<< HEAD
=======
#############추가1엔드
>>>>>>> 7d33ea541317b3b907e7618106820dc8e91fcd84
      

@method_decorator(admin_required, name='dispatch')
class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        product = Product(
            name=form.data.get('name'),
            price=form.data.get('price'),
            description=form.data.get('description'),
            stock=form.data.get('stock')
        )
        product.save()
        return super().form_valid(form)

class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm(self.request)
        return context
