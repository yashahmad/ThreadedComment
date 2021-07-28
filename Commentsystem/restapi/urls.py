from django.urls import path 
from .views import *

urlpatterns = [
    path("page/",ListCreatePageAPIView.as_view(),name="get_post_page"),
	path("page/<uuid:pk>/",RetrieveUpdateDestroyPageAPIView.as_view(),name="get_delete_update_page"),
	path("comment/",ListCreateCommentAPIView.as_view(),name="get_post_comment"),
	path("subcomment/",ListCreateSubcommentAPIView.as_view(),name="get_post_subcomment"),
	path("subcomment/<uuid:pk>",RetrieveUpdateDestroySubcommentAPIView.as_view(),name="get_delete_update_subcomment"),

	# Task 1- Get a list of all comments made on a page with a given url
	path("page/<uuid:pk>/all/",ListAllComment.as_view(),name="get_all_comments"),
	# Task 2- Add a new comment on a page with a given url
	path("page/<uuid:pk>/comment/",AddCommentToPage.as_view(),name="post_comment_to_page"),
	# Task 3- Add a new sub comment on an already existing comment as a reply
	path("page/<uuid:pk>/comment/<uuid:cpk>/subcomment",AddCommentToSubComment.as_view(),name="post_comment_to_subcomment"),
	# Task 4- Edit an existing comment
	# Task 5- Delete a single comment or an entire comment thread using comment's identifier
	path("comment/<uuid:pk>",RetrieveUpdateDestroyCommentAPIView.as_view(),name="get_delete_update_comment"),

]