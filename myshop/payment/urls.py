from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('canceled/', views.payment_canceled, name='canceled'),
    path('done/', views.payment_done, name='done')
]

