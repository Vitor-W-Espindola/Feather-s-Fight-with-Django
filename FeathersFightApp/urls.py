from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_with_no_page, name='index_with_no_page'),
    path('register', views.register_page, name='register_page'),
    path('login', views.login_page, name='login_page'),
    path('register/success', views.register_process, name='register'),
    path('login/success', views.login_process, name='login'),
    path('logout', views.logout_process, name='login'),
    path('<int:index_page_id>/', views.index_with_page, name='index_with_page'),
    path('fight/<int:fight_id>/', views.fight, name='fight'),
    path('dashboard/fight_preview/<int:publication_id>/', views.fight_preview, name='fight_preview'),
    path('dashboard/edit/<int:publication_id>/', views.fight_edit, name='fight_preview'),
    path('dashboard/delete/<int:publication_id>/', views.fight_delete, name='fight_preview'),
    path('dashboard/new', views.new_publication_page, name='new_publication_page'),
    path('dashboard/new/send', views.new_publication_request, name='new_publication_request'),
    path('dashboard', views.dashboard, name='fight'),
]
