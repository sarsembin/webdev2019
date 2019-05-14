from django.urls import path
from api import views

urlpatterns = [
    path('task_lists/', views.category_list),
    path('task_lists/<int:pk>/', views.category_detail),
    path('task_lists/<int:pk>/tasks/', views.category_product)
]
