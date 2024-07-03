from django.urls import path
from futbolistas import views

urlpatterns = [
    path('', views.index_pil, name='index_pil'),
    path('futbolistas_rest/', views.futbolistas_rest, name='futbolistas_rest'),
    path('directors_rest/', views.directors_rest, name='directors_rest'),
    path('estadios_rest/', views.estadios_rest, name='estadios_rest'),
    path('users_rest/', views.users_rest, name='users_rest'),
    path('new_futbolista/', views.NewFutbolistaView.as_view(), name='new_futbolista'),
    path('new_director/', views.NewDirectorView.as_view(), name='new_director'),
    path('new_estadio/', views.NewEstadioView.as_view(), name='new_estadio'),
    path('new_userp/', views.NewUserView.as_view(), name='new_userp'),
]
