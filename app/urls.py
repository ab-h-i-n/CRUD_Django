
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_Page, name='home'),
    path('create/', views.create_Page, name='create'),
    path('list/', views.list_Page, name='list'),
    path('delete/<pk>',views.delete, name = 'delete'),
    path('edit/<pk>',views.edit,name="edit")
]
