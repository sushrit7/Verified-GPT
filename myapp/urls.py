from django.urls import path
from . import views
from .views import question_list, add_question, add_comment, upvote_comment, upvote_answer,downvote_answer,downvote_comment, deleteAll

urlpatterns = [
   # path("", views.home, name="home"),
    path("", question_list, name="question_list"),
    path("add_question/", add_question, name="add_question"),
    path("add_comment/<int:answer_id>/", add_comment, name="add_comment"),
    path("upvote_comment/<int:comment_id>/", upvote_comment, name="upvote_comment"),
    path("upvote_answer/<int:answer_id>/", upvote_answer, name="upvote_answer"),
    path("downvote_comment/<int:comment_id>/", downvote_comment, name="downvote_comment"),
    path("downvote_answer/<int:answer_id>/", downvote_answer, name="downvote_answer"),
    path("delete_all/", deleteAll, name="delete_all"),
    path("thread/", views.thread, name="thread")
]