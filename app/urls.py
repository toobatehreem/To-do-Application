from django.urls import path
from . import views
from .views import Adding
app_name = 'app'

urlpatterns  = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('add', Adding.as_view(), name='add_todo'),
    path('delete_todo', views.delete_todo, name='delete_todo')
]