from django.urls import path, include
from hw_celery import views

urlpatterns = [
    path('reminder/', views.reminder, name='reminder')
]
