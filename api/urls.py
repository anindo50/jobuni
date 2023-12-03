from django.contrib import admin
from django.urls import path
from api import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('signup/', views.signup, name= 'signup'),
    path('profile/', views.profile, name='profile'),
    path('', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('payform/', views.payform, name= 'payform'),
    path('search/', views.search_bar, name= 'search'),
    path('search_result', views.search_result, name= 'search_result'),
    path('test/', views.test, name='test'),
    path('test2/', views.test2, name='test2'),
    path('api/', views.api, name='api'),
    path('edit/', views.edit_profile, name='edit'),
    path('seller/', views.signup_sell, name='seller'),
    path('seller_login/', views.sell_login, name='seller_login'),
    path('sellprofile/', views.sell_profile, name='sellprofile'),
    path('adminlogin/', views.admin_login, name = 'adminlogin'),
    path('adminsign/', views.adminsign, name = 'adminsign'),
    path('admin_page/', views.admin_page, name = 'admin_page'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('user_info/', views.user_info, name='user_info')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)