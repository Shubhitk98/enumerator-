from django.urls import include, path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('about.html/', views.about, name='about' ),
    path('contact.html/', views.contact, name='contact' ),
    path('mentors.html/', views.mentors, name='mentors' ),
    path('register.html/', views.register, name='register' ),
    path('register.html', views.register_submission, name='register_submission' ),
    path('login.html/', views.login, name='login' ),

    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)