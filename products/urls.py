from django.urls import path
from products.views import ProductView


app_name = 'products'

urlpatterns = [
    path('', ProductView.as_view(), name='index'),
]
