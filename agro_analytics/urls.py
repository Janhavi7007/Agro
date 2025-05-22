from turtle import home
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from agroapp import views
from agroapp import views

from agroapp.views import user_dashboard, get_state_schemes 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Basic Pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('submit_contact/', views.submit_contact, name='submit_contact'),


    # Authentication
  


    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    #from user dashboard
    path('schemes/', views.schemes, name='schemes'),
    path('scheduling/', views.scheduling, name='scheduling'),
    path('organic/', views.organic, name='organic'),
    path('disease/', views.disease, name='disease'),
    path('get_farming_category/<slug:category_slug>/', views.get_farming_category, name='get_farming_category'),
    path('weather/', views.weather, name='weather'),
    path('dashboard/state/<str:state_name>/', get_state_schemes, name='get_state_schemes'),
    path('agriculture-news/', views.agriculture_news, name='agriculture_news'),
    path('marketplace/', views.marketplace_view, name='marketplace'),
    path('get_nearby_markets/', views.get_nearby_markets, name='get_nearby_markets'),
    path('agro-business/', views.agro_business_list, name='agro_business_list'),
    path('agro-business/<int:id>/', views.agro_business_detail, name='agro_business_detail'),
    path('agro-business/add/', views.agro_business_create, name='agro_business_create'),
    path('agro-business/<int:pk>/edit/', views.agro_business_update, name='agro_business_update'),
    path('agro-business/<int:pk>/delete/', views.agro_business_delete, name='agro_business_delete'),
    path('update-email/', views.update_email, name='update_email'),
    path('update-password/', views.update_password, name='update_password'),
    path('update-phone/', views.update_phone, name='update_phone'),
    path('feedback/', views.submit_feedback, name='submit_feedback'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
