from django.urls import path
from .views import *

urlpatterns = [
    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetails.as_view()),
    path('location/', LocationList.as_view()),
    path('location/<int:pk>', LocationDetails.as_view()),
    path('order/', OrderList.as_view()),
    path('order/<int:pk>', OrderDetail.as_view()),
]
