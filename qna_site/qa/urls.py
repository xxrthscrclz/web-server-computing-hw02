"""
[과제 3] qa/urls.py
TODO: 질문 목록, 질문 상세, 질문 작성 URL 패턴을 완성하세요.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='question_list'),

    path('question/<int:pk>/', views.question_detail, name='question_detail'),

    path('ask/', views.ask_question, name='ask_question'),
]
