from django.shortcuts import get_object_or_404, render
from darknet.models import Post

def post(request, slug):
	p = get_object_or_404(Post, slug = slug)
	return render(request, 'darknet_post.html', {'post':p})

def posts(request):
	p = Post.objects.all().order_by('-date')
	return render(request, 'darknet_main.html', {'posts':p})
