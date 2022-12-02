from django.shortcuts import render, redirect
from .models import Blog
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(ListView):
    template_name = 'blog/home.html'
    model = Blog
    context_object_name = 'blogs'

class AuthorBlog(ListView):
    model = Blog
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = context['blogs'].filter(user=self.request.user)
        # context['count'] = context['blogs'].filter(complete=False).count()

        # search_input = self.request.GET.get('search-area') or ''
        # if search_input:
        #     context['blogs'] = context['blogs'].filter(
        #         title__contains=search_input)

        # context['search_input'] = search_input

        return context

class BlogCreate(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'description', 'image']
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BlogCreate, self).form_valid(form)

class BlogUpdate(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ['title', 'description', 'image']
    success_url = reverse_lazy('profile')

class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Blog
    context_object_name = 'blog'
    success_url = reverse_lazy('profile')
    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)

class BlogDetail(DetailView):
    model = Blog
    context_object_name = 'blog'

class CustomLoginView(LoginView):
    template_name = 'blog/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('profile')

class AuthorRegistration(FormView):
    template_name = 'blog/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(AuthorRegistration, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('profile')
        return super(AuthorRegistration, self).get(*args, **kwargs)