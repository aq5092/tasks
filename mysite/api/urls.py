from django.urls import path
from . import views

urlpatterns = [
    path("api/", views.TaskDetail.as_view(), name='api'),
    path("api/<int:id>/",views.TaskInfo.as_view())
    #path("api/<int:pk>/", views.TaskDetail.as_view({'get':'retrieve'})),
    #path('api/<int:pk>/', views.TaskUpdate.as_view({'put': 'update'}))
    #path('api/<int:pk>/', views.TaskAPIUpdate.as_view())


]
