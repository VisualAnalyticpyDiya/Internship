from django.urls import path
from . import views
urlpatterns = [
    path('', views.product_page, name ='product_page'),
    path('api/', views.product_api, name='product_api')

]