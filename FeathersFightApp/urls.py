from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:fight_id>/', views.fight, name='fight'),
]
