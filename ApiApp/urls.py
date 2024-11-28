from . import views
from django.urls import path

urlpatterns = [
    path('authors/', views.AuthorList.as_view()),
    path('books/', views.BookList.as_view()),
    path('orders/', views.OrderList.as_view()),
    path('order-items/', views.OrderItemList.as_view()),
    ]