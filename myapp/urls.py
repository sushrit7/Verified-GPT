from django.urls import path
from . import views
from .views import question_list, add_question, add_answer, add_comment, upvote_comment, upvote_answer,downvote_answer,downvote_comment

urlpatterns = [
   # path("", views.home, name="home"),
    path("", question_list, name="question_list"),
    path("add_question/", add_question, name="add_question"),
    path("add_answer/<int:question_id>/", add_answer, name="add_answer"),
    path("add_comment/<int:answer_id>/", add_comment, name="add_comment"),
    path("upvote_comment/<int:comment_id>/", upvote_comment, name="upvote_comment"),
    path("upvote_answer/<int:answer_id>/", upvote_answer, name="upvote_answer"),
    path("downvote_comment/<int:comment_id>/", downvote_comment, name="upvote_comment"),
    path("downvote_answer/<int:answer_id>/", downvote_answer, name="upvote_answer"),

]