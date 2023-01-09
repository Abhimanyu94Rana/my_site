from django.shortcuts import render
from datetime import date
# Create your views here.


all_posts = [
    {
        'slug':'hike-in-the-mountains',
        'image':'mountains.jpg',
        'author':'Tom',
        'date':date(2023,1,6),
        'title':'Mountain Hiking',
        'excerpt':'some text',
        'content':"""
            lorem ipsum text comes to the picture
            lorem ipsum text comes to the picture
            lorem ipsum text comes to the picture
            lorem ipsum text comes to the picture
            lorem ipsum text comes to the picture
            lorem ipsum text comes to the picture
            lorem ipsum text comes to the picture
        """
    }
]

def get_date(post):
    return post['date']

def starting_page(request):
    # sorted_posts = all_posts.sort(key=get_date)
    sorted_posts = sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request,"blog/index.html",{
        "posts":latest_posts
    })

def posts(request):
    return render(request,"blog/all-posts.html",{
        "all_posts":all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html",{
        "post":identified_post
    })