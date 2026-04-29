"""
[과제 3] qa/views.py
TODO: 질문 목록, 질문 상세, 질문 작성 뷰를 완성하세요.
"""
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User


def question_list(request):
    """질문 목록 뷰: 최신순으로 정렬된 모든 질문을 표시"""
    questions = Question.objects.order_by('-created_at')

    return render(request, 'qa/question_list.html', {'questions': questions})


def question_detail(request, pk):
    """질문 상세 뷰: 질문 내용과 답변 목록을 표시하고, 답변 작성 처리"""
    question = get_object_or_404(Question, pk=pk)

    if request.method == 'POST':
        content = request.POST.get('content')
        if content and request.user.is_authenticated:
            Answer.objects.create(
                question=question,
                content=content,
                author=request.user,
                created_at=timezone.now()
            )
            return redirect('question_detail', pk=pk)

    return render(request, 'qa/question_detail.html', {'question': question})


@login_required
def ask_question(request):
    """질문 작성 뷰: 로그인한 사용자만 질문을 작성할 수 있음"""
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Question.objects.create(
                title=title,
                content=content,
                author=request.user,
                created_at=timezone.now()
            )
            return redirect('question_list')

    return render(request, 'qa/ask_question.html')
