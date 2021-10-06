from django.urls import path
from .views import *

urlpatterns = [
    path('', first_page, name='home'),
    path('thanks/', thanks_page, name='thanks_page')
]