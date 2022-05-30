from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from base.models import Task


class Login(LoginView):
  template_name = 'base/login.html'
  fields = '__all__'
  redirect_authenticated_user = True

  def get_success_url(self) -> str:
    return reverse_lazy('tasks')


class TaskList(LoginRequiredMixin, ListView):
  model = Task
  context_object_name = 'tasks'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['tasks'] = context['tasks'].filter(user=self.request.user)
    context['count'] = context['tasks'].filter(complete=False).count()

    return context


class TaskDetail(LoginRequiredMixin, DetailView):
  model = Task
  context_object_name = 'task'
  template_name = 'base/task.html'


class CreateTask(LoginRequiredMixin, CreateView):
  model = Task
  fields = ['title', 'description', 'complete']
  success_url = reverse_lazy('tasks')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(CreateTask, self).form_valid(form)


class UpdateTask(LoginRequiredMixin, UpdateView):
  model = Task
  fields = ['title', 'description', 'complete']
  success_url = reverse_lazy('tasks')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(UpdateTask, self).form_valid(form)


class DeleteTask(LoginRequiredMixin, DeleteView):
  model = Task
  context_object_name = 'task'
  success_url = reverse_lazy('tasks')