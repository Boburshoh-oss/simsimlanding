from django.urls import path
from .views import ProjectView, ProjectDetailView

urlpatterns = [
    path('', ProjectView.as_view(), name='project'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
]