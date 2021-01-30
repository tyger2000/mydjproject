from django.shortcuts import render, get_object_or_404
from .models import blog_project

# Create your views here.
def all_blogs(request):
	blogp = blog_project.objects.all()
	return render(request, 'blog/all_blogs.html', {'blogp': blogp})

def detail(request, blog_id):
	blog = get_object_or_404(blog_project, pk= blog_id)
	return render(request, 'blog/detail.html', {'blog': blog})
