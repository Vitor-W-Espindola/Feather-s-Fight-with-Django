from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_with_no_page, name='index_with_no_page'),
    path('register', views.register, name='register'),
    path('<int:index_page_id>/', views.index_with_page, name='index_with_page'),
    path('<int:index_page_id>/fight/<int:fight_id>/', views.fight, name='fight'),
]
