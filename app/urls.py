from django.urls import path

from app import views

urlpatterns = [
    path('', views.home),
    path('ItemList', views.ItemList.as_view()),
    path('ItemDetail/<int:pk>', views.ItemDetail.as_view())
]
