from django.urls import path
from hw_celery import views

urlpatterns = [
    path('reminder/', views.reminder, name='reminder'),
    path('author/', views.authors, name='author'),
    path('author/<pk>', views.authors_info, name='authors_info'),
    path('quote/', views.quote, name='quote')
]
