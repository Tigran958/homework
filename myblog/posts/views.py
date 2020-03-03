from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Author


# Create your views here.

def first_post(request):
	first_post = Post.objects.all()[0]
	return HttpResponse(first_post.author.name + first_post.content + first_post.headline + str(first_post.creation_date))

def second_post(request):
	second_post = Post.objects.all()[1]
	print(Author.objects.get(name="Name").email)
	return HttpResponse(second_post.author.name + second_post.content + second_post.headline + str(second_post.creation_date))
 