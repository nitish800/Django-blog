from django.shortcuts import render
from .models import BlogPost,Categories


# Create your views here.

def index(request):
    post_title_list = BlogPost.objects.order_by('-post_date')[:5]
    context = {'post_title_list':post_title_list}
    return render(request,'index.html',context)
    

def post(request):
    return
        