from django.shortcuts import render
from django.shortcuts import render

from django.views.generic import ListView,DetailView
from django.shortcuts import get_object_or_404
from requests import request
from .forms import CommentForm, ComplainForm

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.contrib.auth.decorators import login_required


from .models import comaplain,Comment
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib import messages




class HomeView(LoginRequiredMixin,ListView):
    template_name = 'home.html'
    queryset = comaplain.objects.all()
    paginate_by = 2



class PostView(DetailView):
    model = comaplain
    template_name = "post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        slug = self.kwargs["slug"]

        form = CommentForm()
        post = get_object_or_404(comaplain, pk=pk, slug=slug)
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        post = comaplain.objects.filter(id=self.kwargs['pk'])[0]
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            comment = Comment.objects.create(
                name=name, email=email, content=content, post=post
            )

            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)

        return self.render_to_response(context=context)   



class PostCreateView(LoginRequiredMixin, CreateView):
    model = comaplain
    fields = ["title", "content","assign"]
    template_name = 'complain_form.html'
    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been created successfully.')
        return reverse_lazy("home")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.slug = slugify(form.cleaned_data['title'])
        obj.save()
        return super().form_valid(form)
class PostUpdateViewadmin(LoginRequiredMixin, UpdateView):
    model = comaplain
   
    fields = ["title", "status"]
    template_name = 'complain_form.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update

        return context

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been updated successfully.')
        return reverse_lazy("home")

    def get_queryset(self):
        return self.model.objects.all() 

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = comaplain
    template_name = 'complain_form.html'
    
   
    fields = fields = ["title", "status","content"] 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update

        return context

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been updated successfully.')
        return reverse_lazy("home")

    def get_queryset(self):
        return self.model.objects.all()

      
    



      