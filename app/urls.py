
from django.urls import path
from . import views
urlpatterns = [
    path("",views.getRoutes,name="Routes"),
    path("products/",views.getProducts,name="products"),
    path("products/<pk>/",views.getProduct,name="products"),


]
