from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import (CreateView,
                                  ListView,
                                  UpdateView)
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm


class IndexClass(LoginRequiredMixin, CreateView):
    template_name = "index.html"
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('load')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.user_id
        return super().form_valid(form)

class LoadClass(LoginRequiredMixin, ListView):
    template_name = "load.html"
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.user.user_id
        queryset = queryset.filter(user_id=user_id)
        for omit in queryset:
            omit.memo = omit.memo[:20] + '...' if len(omit.memo) > 20 else omit.memo
        return queryset
    

class EditClass(LoginRequiredMixin, UpdateView):
    template_name = "edit.html"
    model = Post
    fields = ('memo',)
    success_url = reverse_lazy('load')

@require_POST
def delete(request, pk):
    post = get_object_or_404(Post, memo_id=pk)
    post.delete()
    return redirect('/load')