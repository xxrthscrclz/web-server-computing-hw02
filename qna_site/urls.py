"""
[과제 3] qna_site/urls.py
TODO: qa 앱의 URL을 포함(include)하고, 로그인/로그아웃 URL을 추가하세요.
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('qa.urls')),

    path('login/', auth_views.LoginView.as_view(template_name='qa/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
