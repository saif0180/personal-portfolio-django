from django.shortcuts import render, get_object_or_404
from .models import Blog
def blogs(request):
    blobs = Blog.objects.order_by('-date')
    return render(request, 'blog/blogs.html', {'blog':blobs})
def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})