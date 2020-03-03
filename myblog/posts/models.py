from django.db import models

class Author(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()

	def __str__(self):
		return self.name

class Post(models.Model):
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	headline = models.CharField(max_length=200)
	content = models.TextField()
	creation_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.headline

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	comment_text = models.CharField(max_length=100)
	creation_date = models.DateTimeField(auto_now_add=True)
# Create your models here.
