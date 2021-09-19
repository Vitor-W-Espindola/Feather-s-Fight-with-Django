from django.urls import path

from FeathersFightApp.views.index import *
from FeathersFightApp.views.register import *
from FeathersFightApp.views.login import *
from FeathersFightApp.views.dashboard import *
from FeathersFightApp.views.admin_dashboard import *

urlpatterns = [

    # index.py
    path('', index_with_no_page, name='index_with_no_page'),
    path('<int:index_page_id>/', index_with_page, name='index_with_page'),
    path('fight/<int:fight_id>/', fight, name='fight'),

    # register.py
    path('register', register_page, name='register_page'),
    path('register/success', register_process, name='register'),

    # register_author.py
    path('register_author', register_author_page, name='register_page'),
    path('register_author/success', register_author_process, name='register'),

    # login.py
    path('login', login_page, name='login_page'),
    path('login/success', login_process, name='login'),
    path('logout', logout_process, name='login'),

    # dashboard.py
    path('dashboard', dashboard, name='dashboard_page'),
    path('dashboard/fight_preview/<int:publication_id>/', fight_preview, name='fight_preview_page'),
    path('dashboard/new', new_publication_page, name='new_publication_page'),
    path('dashboard/new/send', new_publication_request, name='new_publication_request_send'),
    path('dashboard/new/save', new_save, name='save_pub'),
    path('dashboard/new/save/dashboard', new_save_go_to_dashboard, name='save_pub_go_to_dashboard'),
    path('dashboard/edit/<int:save_id>', edit_publication_page, name='edit_pub_page_send'),
    path('dashboard/edit/save/<int:save_id>', edit_save, name='save_pub'),
    path('dashboard/edit/save/dashboard/<int:save_id>', edit_save_go_to_dashboard, name='save_pub_go_to_dashboard'),
    path('dashboard/delete/save/<int:save_id>', delete_save, name='save_pub'),
    path('dashboard/delete/<int:publication_id>/', fight_delete, name='delete_pub'),
    path('dashboard/request_preview/<int:request_id>', request_preview, name='request_preview_page'),
    path('dashboard/submit/save/<int:save_id>', submit_save, name='submit_save'),
    path('dashboard/submit/new', submit_new, name='submit_new'),

    # admin_dashboard.py
    path('admin_dashboard', admin_dashboard, name='admin_dashboard_page'),
    path('admin_preview_request/<int:request_id>', admin_preview_request, name='admin_preview-page'),
    path('admin_preview/<int:pub_id>', admin_preview, name='admin_preview-page'),
    path('admin_dashboard/approve/<int:request_id>', admin_approve, name='admin_approve'),
    path('admin_dashboard/decline/<int:request_id>', admin_decline, name='admin_decline'),
    path('admin_dashboard/delete/<int:pub_id>', admin_delete, name='admin_delete')
]
