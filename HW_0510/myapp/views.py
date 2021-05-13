from django.shortcuts import get_object_or_404, render
from .models import Blog
from .models import Two
from .models import Three
from .models import Four
from .models import Five
# Create your views here.
def home(request):
    return render(request, 'home.html')

def blog(request):
    bloginput = Blog.objects.all()
    return render(request, 'blog.html', {'blog':bloginput})

def two(request):
    input = Two.objects.all()
    return render(request, 'two.html', {'input':input})

def three(request):
    input = Three.objects.all()
    return render(request, 'three.html', {'input':input})

def four(request):
    input = Four.objects.all()
    return render(request, 'four.html', {'input':input})
    
def five(request):
    input = Five.objects.all()
    return render(request, 'five.html', {'input':input})    

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html',{'blog':blog})