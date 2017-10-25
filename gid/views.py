from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from gid.forms import OtForm ,TyrForm
from gid.models import Ot, Tyr
from django.contrib.auth.decorators import login_required



def glav(request):
    return render(request, 'glav.html', {})
'''
def ot_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'chat.html', {'posts': posts})
'''

def ot_new(request, pk):
    post = get_object_or_404(Tyr, pk=pk)
    if request.method == "POST":
        form = OtForm(request.POST)
        if form.is_valid():
            ot = form.save(commit=False)
            ot.post = post
            ot.save()
            return redirect('gid/agents_detail.html', pk=post.pk)
    else:
        form = OtForm()
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
    ports = Tyr.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'gid/agents.html', {'ports':ports})

def tyr_detail(request, pk):
    port = get_object_or_404(Tyr, pk=pk)
    return render(request, 'gid/agents_detail.html', {'port': port})

@login_required
def tyr_remove(request, pk):
    ot = get_object_or_404(Ot, pk=pk)
    ot.delete()
    return redirect('agents_detail', pk=p.pk)

@login_required
def tyr_approve(request, pk):
    ot = get_object_or_404(Ot, pk=pk)
    ot.approve()
    return redirect('agents_detail', pk=ports.pk)

def about(request):
    return render(request, 'about.html', {})

def images(request):
    return render(request, 'images.html', {})