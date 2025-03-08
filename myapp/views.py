from django.shortcuts import render, redirect
from .models import Question, Answer, Comment

def question_list(request):
    questions = Question.objects.all()
    return render(request, "base.html", {"questions": questions})

def add_question(request):
    if request.method == "POST":
        question_text = request.POST.get("question_text")
        print(f"After deletion - Questions: {Question.objects.count()}, Answers: {Answer.objects.count()}, Comments: {Comment.objects.count()}")
        if question_text:
            question = Question.objects.create(text=question_text)
            answer_text = "Call the API maybe"
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

def deleteAll(request):
    # Print the number of objects before deletion
    print(f"Before deletion - Questions: {Question.objects.count()}, Answers: {Answer.objects.count()}, Comments: {Comment.objects.count()}")
    
    # Deleting all objects
    Comment.objects.all().delete()
    Answer.objects.all().delete()
    Question.objects.all().delete()
    
    # Print the number of objects after deletion (should be 0)
    print(f"After deletion - Questions: {Question.objects.count()}, Answers: {Answer.objects.count()}, Comments: {Comment.objects.count()}")
    
    # Redirect to the question list
    return redirect("question_list")

