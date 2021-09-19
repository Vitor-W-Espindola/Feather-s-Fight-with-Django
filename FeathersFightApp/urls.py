from django.urls import path

from FeathersFightApp.views.index import *
from FeathersFightApp.views.register import *
from FeathersFightApp.views.register_author import *
from FeathersFightApp.views.login import *
from FeathersFightApp.views.dashboard import *
from FeathersFightApp.views.admin_dashboard import *


urlpatterns = [

    # index.py
    path('', index_with_no_page, name='index_with_no_page'),
    path('<int:index_page_id>/', index_with_page, name='index_with_page'),
    path('article/<int:article_id>/', article, name='article'),

    # register.py
    path('register', register_page, name='register_page'),
    path('register/success', register_process, name='register_success'),

    # register_author.py
    path('register_author', register_author_page, name='register_author_page'),
    path('register_author/success', register_author_process, name='register_author_success'),

    # login.py
    path('login', login_page, name='login_page'),
    path('login/success', login_process, name='login_success'),
    path('logout', logout_process, name='logout'),

    # dashboard.py
    path('dashboard', dashboard, name='dashboard_page'),
    
    path('dashboard/article_preview/<int:article_id>', article_preview, name='article_preview'),

    path('dashboard/new', new_article_page, name='new_article_page'),
    path('dashboard/new/save', new_article_save_and_keep_writing, name='new_article_save_and_keep_writing'),
    path('dashboard/new/save/dashboard', new_article_save_and_go_to_dashboard, name='edit_save_save_and_go_to_dashboard'),
    path('dashboard/new/submit', new_article_request, name='new_article_request'),

    path('dashboard/edit/<int:article_save_id>', edit_save, name='edit_save'),
    path('dashboard/edit/save/<int:article_save_id>', edit_save_save_and_keep_writing, name='edit_save_save_and_keep_writing'),
    path('dashboard/edit/save/dashboard/<int:article_save_id>', edit_save_save_and_go_to_dashboard, name='edit_save_save_and_go_to_dashboard'),
    path('dashboard/edit/submit/<int:article_save_id>', edit_save_submit, name='edit_save_submit'),
    
    path('dashboard/delete/save/<int:article_save_id>', delete_save, name='delete_save'),
    
    path('dashboard/article_request_preview/<int:article_request_id>', article_request_preview, name='article_request_preview'),
    

    # admin_dashboard.py
    path('admin_dashboard', admin_dashboard, name='admin_dashboard'),
    
    path('admin_dashboard/admin_article_request_preview/<int:article_request_id>', admin_article_request_preview, name='admin_preview_article_request'),
    path('admin_dashboard/admin_article_preview/<int:article_id>', admin_article_preview, name='admin_preview_article'),
    
    path('admin_dashboard/approve/<int:article_request_id>', admin_approve, name='admin_approve'),
    path('admin_dashboard/decline/<int:article_request_id>', admin_decline, name='admin_decline'),

    path('admin_dashboard/delete/<int:article_id>', admin_delete, name='admin_delete')
]
