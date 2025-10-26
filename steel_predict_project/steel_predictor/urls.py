from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predict/<str:steel_type>/', views.predict_view, name='predict'),
    path('result/', views.result_view, name='result'),
]
