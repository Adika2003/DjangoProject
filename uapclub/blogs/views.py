from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def blog_list(request):
    blogs = BlogPost.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blogs/blog_list.html', {'blogs': blogs})

def blog_detail(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug, published=True)
    return render(request, 'blogs/blog_detail.html', {'blog': blog})

@login_required
def blog_create(request):
    if not request.user.is_staff:
        messages.error(request, 'Only staff can create blogs.')
        return redirect('blogs:blog_list')
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            b = form.save(commit=False)
            b.author = request.user
            b.save()
            messages.success(request, 'Blog published.')
            return redirect('blogs:blog_detail', slug=b.slug)
    else:
        form = BlogForm()
    return render(request, 'blogs/blog_form.html', {'form': form})
