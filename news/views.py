from re import template
from unicodedata import category, name
from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date
# Create your views here.
from .forms import *

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        posts = Post.objects.order_by('-created_date').filter(is_feature=True)[0:5]
        for post in posts:
            post.created_date_format = post.created_date.strftime("Ngày %d tháng %m năm %Y")
        feature_post = posts[0]
        tags = Tag.objects.all()
        all_posts = Post.objects.all()
        for post in all_posts:
            post.created_date_format = post.created_date.strftime("Ngày %d tháng %m năm %Y")
        paginator = Paginator(all_posts,4)
        page = request.GET.get('page', 1)
        today = date.today()
        days = ["Thứ hai", "Thứ ba", "Thứ tư", "Thứ năm", "Thứ sáu", "Thứ bảy", "Chủ nhật"]
        dateNow = days[today.weekday()] + " " +today.strftime("Ngày %d tháng %m năm %Y")
        # Popular post
        popularPost = Post.objects.order_by('-count_access').all()[0:4]
        for post in popularPost:
            post.created_date_format = post.created_date.strftime("Ngày %d tháng %m năm %Y")
        trendingPost = Post.objects.order_by('-created_date').filter(is_trending=True)[0:5]
        for post in trendingPost:
            post.created_date_format = post.created_date.strftime("Ngày %d tháng %m năm %Y")
        categories = Category.objects.all()
        try:
            pposts = paginator.page(page)
        except PageNotAnInteger:
            pposts = paginator.page(1)
        except EmptyPage:
            pposts = paginator.page(paginator.num_pages)

        return render(request, self.template_name,{'posts':posts[1:],'tags':tags,'pposts':pposts,
        'dateNow':dateNow,'feature_post':feature_post,'popularPost':popularPost,'trendingPost':trendingPost,
        'categories':categories})
class PostDetail(DetailView):
    model = Post
    template_name = 'detail.html'
    def get(self, request,*args, **kwargs):
        post = Post.objects.get(pk=self.kwargs.get('pk'))
        post.created_date_format = post.created_date.strftime("Ngày %d tháng %m năm %Y")
        post.count_access += 1
        post.save()
        today = date.today()
        days = ["Thứ hai", "Thứ ba", "Thứ tư", "Thứ năm", "Thứ sáu", "Thứ bảy", "Chủ nhật"]
        dateNow = days[today.weekday()] + " " +today.strftime("Ngày %d tháng %m năm %Y")
        popularPost = Post.objects.order_by('-count_access').all()[0:4]
        tags = post.tags.all()
        categories = Category.objects.all()
        trendingPost = Post.objects.order_by('-created_date').filter(is_trending=True)[0:5]
        for post in popularPost:
            post.created_date_format = post.created_date.strftime("Ngày %d tháng %m năm %Y")
        for post in trendingPost:
                    post.created_date_format = post.created_date.strftime("Ngày %d tháng %m năm %Y")           
        return render(request, self.template_name,{'post':post,'tags':tags,'popularPost':popularPost,
        'dateNow':dateNow,'trendingPost':trendingPost,'categories':categories})
class CategoryView(ListView):
    model = Post
    template_name = 'category.html'
    def get(self, request,*args, **kwargs):
        slug = self.kwargs.get('slug')
        currentCategory = Category.objects.get(slug=slug)
        posts  = Post.objects.filter(category=currentCategory)
        for post in posts:
            post.created_date_format = post.created_date.strftime("Ngày %d tháng %m năm %Y")
        paginator = Paginator(posts,4)
        page = request.GET.get('page', 1)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        categories = Category.objects.all()
        today = date.today()
        days = ["Thứ hai", "Thứ ba", "Thứ tư", "Thứ năm", "Thứ sáu", "Thứ bảy", "Chủ nhật"]
        dateNow = days[today.weekday()] + " " +today.strftime("Ngày %d tháng %m năm %Y")
        return render(request, self.template_name,{'posts':posts,'category_name':currentCategory.name.title(),
        'categories':categories,'dateNow':dateNow})

def getContact(request):
    categories = Category.objects.all()
    today = date.today()
    days = ["Thứ hai", "Thứ ba", "Thứ tư", "Thứ năm", "Thứ sáu", "Thứ bảy", "Chủ nhật"]
    dateNow = days[today.weekday()] + " " +today.strftime("Ngày %d tháng %m năm %Y")
    return render(request,'contact.html',{'categories':categories,'dateNow':dateNow})