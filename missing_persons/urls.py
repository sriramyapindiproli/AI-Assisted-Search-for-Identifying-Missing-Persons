
from django.contrib import admin
from django.urls import path
from mainapp import views as mainapp_views
from adminapp import views as admin_views
from userapp import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #main
    path('admin/', admin.site.urls),
    path('',mainapp_views.main_home,name="main_home"),
    path('main-about',mainapp_views.main_about,name="main_about"),
    path('main-contact',mainapp_views.main_contact,name="main_contact"),
    path('main-policelogin',admin_views.main_policelogin,name="main_policelogin"),
    path('main-userlogin',user_views.main_userlogin,name="main_userlogin"),
    path('main-userregistration',user_views.main_userregistration,name="main_userregistration"),
    
    #user
    path('user-dashboard',user_views.user_dashboard,name="user_dashboard"),
    path('user-registercase',user_views.user_registercase,name="user_registercase"),
    path('user-cases',user_views.user_cases,name="user_cases"),
    path('user-feedback',user_views.user_feedback,name="user_feedback"),
    path('user-myprofile',user_views.user_myprofile,name="user_myprofile"),
    path('user-status',user_views.user_status,name="user_status"),
    
    #admin
    path('admin-addnewcase',admin_views.admin_addnewcase,name="admin_addnewcase"),
    path('admin-casesanalysisgraph',admin_views.admin_casesanalysisgraph,name="admin_casesanalysisgraph"),
    path('admin-dashboard',admin_views.admin_dashboard,name="admin_dashboard"),
    path('admin-editmanagecases/<int:add_id>',admin_views.admin_editmanagecases,name="admin_editmanagecases"),
    path('admin-managecases',admin_views.admin_managecases,name="admin_managecases"),
    path('admin-sentimentgraph',admin_views.admin_sentimentgraph,name="admin_sentimentgraph"),
    path('admin-viewusersubmittedcases',admin_views.admin_viewusersubmittedcases,name="admin_viewusersubmittedcases"),
    path('admin-find-match',admin_views.admin_find_match,name='admin_find_match'),
    path('admin-match-person/<int:id>',admin_views.admin_match_person,name='admin_match_person'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
