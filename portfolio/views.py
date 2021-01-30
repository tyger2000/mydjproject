from django.shortcuts import render
from .models import Project


# Create your views here.
def home(request):
	project = Project.objects.all() #   .order_by('-date')[:5] To show upto 5 instances
	return render(request, 'portfolio/home.html', {'project': project})

def show_blog(request):
	return render(request, 'blog/all_blogs.html')
