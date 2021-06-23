from django.urls import path
# function routes from views.py
from .views import lead_list, lead_detail

app_name = 'leads'

urlpatterns = [
    path('', lead_list),
    path('<id>', lead_detail)
    ]