from ast import arg
from pyexpat import model
from django.urls import reverse
from distutils import archive_util
from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
		#return reverse('article-detail', args=(str(self.id)) )
        return reverse('home')
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=False,unique=True)
    # Edit slug to auto generate from name
    def __str__(self):
        return self.name
    def get_absolute_url(self):
		#return reverse('article-detail', args=(str(self.id)) )
        return reverse('test')

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    feature_image = models.ImageField(upload_to = 'news/static/img_post')
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    tag_id = models.ManyToManyField(Tag,related_name='news_tag')
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
		#return reverse('article-detail', args=(str(self.id)) )
        return reverse('home')


