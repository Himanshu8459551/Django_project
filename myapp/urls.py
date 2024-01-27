from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('new/', views.new, name="new"),
    path('contact/', views.contact, name="contact"),
    path('all_member/', views.all_member, name="all_member"),
    path('all_member/detail/<int:id>', views.detail, name="detail"),
    path('all_member/detail/update/<int:id>', views.update, name="update"),
    path('all_member/detail/delete/<int:id>', views.delete, name='delete'),
  
]