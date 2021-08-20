from django.urls import path
# function routes from views.py
from .views import (LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView,
                    LeadDeleteView, AssignAgentView)

app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/update', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete', LeadDeleteView.as_view(), name='lead-delete'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    path('assign-agent/', AssignAgentView.as_view(), name='assign-agent'),

    ]