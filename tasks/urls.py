from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView, toggle_complete
from .views import TaskDetailView

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('add/', TaskCreateView.as_view(), name='task-add'),
    path('toggle/<int:pk>/', toggle_complete, name='task-toggle'),  # neu
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name='task-edit'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]