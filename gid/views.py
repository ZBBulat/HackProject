from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from gid.forms import PostForm, TyrForm
from gid.models import Post, Tyr


def glav(request):
    return render(request, 'glav.html', {})

def ot_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'chat.html', {'posts': posts})

def ot_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('chat.html', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'new_message.html', {'form': form})

def tyr_new(request):
    if request.method == "POST":
        form = TyrForm(request.POST)
        if form.is_valid():
            port = form.save(commit=False)
            port.published_date = timezone.now()
            port.save()
            return redirect('gid/agents.html', pk=port.pk)
    else:
        form = TyrForm()
    return render(request, 'gid/add_agents.html', {'form': form})

def tyrs(request):
    ports = Tyr.objects.all()
    return render(request, 'gid/agents.html', {'ports':ports})

def tyr_detail(request, pk):
    port = get_object_or_404(Tyr, pk=pk)
    return render(request, 'gid/agents_detail.html', {'port': port})