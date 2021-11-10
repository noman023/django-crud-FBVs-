from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update/<int:jersey_no>', views.update, name='update'),
    path('delete/<int:jersey_no>', views.delete, name='delete'),
]