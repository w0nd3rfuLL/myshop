from django.urls import path
from . import views

urlpatterns = [
    path('', views.cloth_list, name='cloth_list'),
    path('<category_slug>/', views.cloth_list, name='cloth_list_by_category'),
    path('<id>/<slug>/', views.cloth_detail, name='cloth_detail'),
    ]
