from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import (CreateView,
                                  ListView,
                                  UpdateView)
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from .models import Post
from .forms import PostForm


class IndexClass(CreateView):
    template_name = "index.html"
    model = Post
    fields = "__all__"
    success_url = reverse_lazy('load')

class LoadClass(ListView):
    template_name = "load.html"
    model = Post
    fields = ('memo', 'date',)
    context_object_name = 'posts'

class EditClass(UpdateView):
    template_name = "edit.html"
    model = Post
    fields = ('memo',)
    success_url = reverse_lazy('load')

#@require_POST
def delete(request, pk):
    post = get_object_or_404(Post, memo_id=pk)
    post.delete()
    return redirect('/load')