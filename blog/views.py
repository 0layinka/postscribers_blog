from django.shortcuts import render, redirect
from .models import postModel
from .forms import postModelForm, commentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    if request.method == 'POST':
        form = postModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect(index)

    else:
        post = postModel.objects.all().order_by('-id')
        form = postModelForm()
        data = {
            'post':post,
            'forms': form
        }

        return render(request, 'blog/blog-index.html', data)

@login_required
def detail(request, pk):
    post = postModel.objects.get(id=pk)
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.post = post 
            instance.save()
            return redirect(detail , post.id)
    else:
        form = commentForm()
        data = {
            'posts': post,
            'comment': form,
        }
        return render(request, 'blog/blog-details.html', data)

@login_required
def edit_post(request, pk):
    post = postModel.objects.get(id=pk)
    if request.method == 'POST':
        form = postModelForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('blog-details', post.id)
    else:
        form = postModelForm(instance=post)
    data = {
        'forms': form
    }
    return render(request, 'blog/edit-blog.html', data)
    
@login_required
def delete_post(request, pk):
    post = postModel.objects.get(id=pk)
    post.delete()
    return redirect('blog-index')




