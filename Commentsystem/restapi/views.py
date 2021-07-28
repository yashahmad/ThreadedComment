from django.db.models import query
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .serializers import PageSerializer, CommentSerializer, SubcommentSerializer
from .models import Page, Comment, Subcomment

class ListCreatePageAPIView(ListCreateAPIView):
	queryset = Page.objects.all()
	serializer_class = PageSerializer

class RetrieveUpdateDestroyPageAPIView(RetrieveUpdateDestroyAPIView):
	queryset = Page.objects.all()
	serializer_class = PageSerializer

class ListCreateCommentAPIView(ListCreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer 

class RetrieveUpdateDestroyCommentAPIView(RetrieveUpdateDestroyAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

class ListCreateSubcommentAPIView(ListCreateAPIView):
	queryset = Subcomment.objects.all()
	serializer_class = SubcommentSerializer

class RetrieveUpdateDestroySubcommentAPIView(RetrieveUpdateDestroyAPIView):
	queryset = Subcomment.objects.all()
	serializer_class = SubcommentSerializer

# Task 1- Get a list of all comments made on a page with a given url
# Task 2- Add a new comment on a page with a given url
# Task 3- Add a new sub comment on an already existing comment as a reply
# Task 4- Edit an esiting comment
# Task 5- Delete a single comment or an entire comment thread using comment's identifier

class AddCommentToPage(CreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

	def post(self, request, *args, **kwargs):
		request.data._mutable = True
		request.data['page_id'] = self.kwargs.get('pk')
		return self.create(request, *args, **kwargs)

class AddCommentToSubComment(CreateAPIView):
	queryset = Subcomment.objects.all()
	serializer_class = SubcommentSerializer

	def post(self, request, *args, **kwargs):
		request.data._mutable = True
		request.data['comment_id'] = self.kwargs.get('cpk')
		return self.create(request, *args, **kwargs)

class ListAllComment(ListAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

	def get_queryset(self):
		page_id = self.kwargs['pk']
		comments = Comment.objects.filter(page_id=page_id).order_by('created')
		return comments