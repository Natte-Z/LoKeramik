from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
    path('connect/<operation>/<pk>', views.change_favourite,
         name='change_favourite')
]
