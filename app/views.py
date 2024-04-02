from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.models import Group


class TodoList(ListView):
    model = Todo
    template_name = 'home.html'
    context_object_name = 'todos'

class TodoDetail(DetailView):
    model = Todo
    template_name = 'detail.html'
    context_object_name = 'todo'

class TodoCreate(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'create.html'
    success_url = reverse_lazy('home')

class TodoUpdate(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'update.html'
    success_url = reverse_lazy('home')

class TodoDelete(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


class SignUp(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')

    # как в группу добавить юзера?
    def form_valid(self, form):
        response = super().form_valid(form)
        group = Group.objects.get(name='SEP_221.1')
        group.user_set.add(self.object)
        
        return response
    

class Login(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('home')

class Logout(LogoutView):
    next_page = reverse_lazy('home')



