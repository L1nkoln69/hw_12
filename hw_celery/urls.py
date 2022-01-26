from django.urls import path
from hw_celery import views

urlpatterns = [
    path('reminder/', views.reminder, name='reminder')
]
