from django.urls import path
  
from projects import views
  
urlpatterns = [
    path('', views.project_index, name='project_index'),
    path('show/<int:pk>', views.project_show, name='project_show'),
    path('new', views.project_create, name='project_new'),
    path('store', views.project_store, name='project_store'),
    path('edit/<int:pk>', views.project_edit, name='project_edit'),
    path('update/<int:pk>', views.project_update, name='project_update'),
    path('delete/<int:pk>', views.project_delete, name='project_delete'),
]