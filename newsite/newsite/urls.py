from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from beerbar.views import TaskViewSet, CreateuserView
from beerbar import views
from django.urls import path
from beerbar import views, models



urlpatterns = [
    path('', views.index, name='index'),
    url('admin/', admin.site.urls),
    path('products', views.products, name='products'),
    path('products_whisky', views.products_whisky, name='whisky'),
    path('products_beer', views.products_beer, name='beer'),
    path('products_wine', views.products_wine, name='wine'),
    path('products_rum', views.products_rum, name='rum'),
    path('products_gin', views.products_gin, name='gin'),
    path('products_mezcal', views.products_mezcal, name='mezcal'),
    path('products_room', views.products_vodka, name='vodka'),
    path('contact', views.contact, name='contact'),
    path('vision', views.vision, name='vision'),
    path('yourorder', views.yourorder, name='yourorder'),
    path("delete/<id>/", views.delete, name='delete'),
    path("add/<name>/<int:price>/<category>", views.add_to_cart, name='add'),
    path('signup/', views.sign_up, name='signup') ,
    path('login/', views.user_login, name ='login'),
    path('profile/', views.user_profile, name='profile'),
    path('logout/', views.user_logout, name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
