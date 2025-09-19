from django.urls import path
from . import views
app_name = 'clubs'

urlpatterns = [
    path('', views.index, name='index'),              # home page
    path('all/', views.club_list, name='club_list'),
    path('create/', views.club_create, name='club_create'),
    path('<int:pk>/', views.club_detail, name='club_detail'),
]
