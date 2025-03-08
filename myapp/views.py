from django.shortcuts import render, redirect
from .models import Question, Answer, Comment

def question_list(request):
    questions = Question.objects.all()
    return render(request, "Questions.html", {"questions": questions})

def add_question(request):
    if request.method == "POST":
        question_text = request.POST.get("question_text")
        if question_text:
            Question.objects.create(text=question_text)
    return redirect("question_list")

def add_answer(request, question_id):
    if request.method == "POST":
        answer_text = request.POST.get("answer_text")
        question = Question.objects.get(id=question_id)
        if answer_text:
            Answer.objects.create(question=question, text=answer_text)
    return redirect("question_list")

def add_comment(request, answer_id):
    if request.method == "POST":
        comment_text = request.POST.get("comment_text")
        answer = Answer.objects.get(id=answer_id)
        if comment_text:
            Comment.objects.create(answer=answer, text=comment_text)
    return redirect("question_list")

def upvote_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.upvotes += 1
    comment.save()
    return redirect("question_list")

def upvote_answer(request, answer_id):
    answer = Answer.objects.get(id=answer_id)
    answer.upvotes += 1
    answer.save()
    return redirect("question_list")

def downvote_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.upvotes -= 1
    comment.save()
    return redirect("question_list")

def downvote_answer(request, answer_id):
    answer = Answer.objects.get(id=answer_id)
    answer.upvotes -= 1
    answer.save()
    return redirect("question_list")
