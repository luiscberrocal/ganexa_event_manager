from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView

from ganexa_event_manager.ex_training.forms import ExerciseForm
from ganexa_event_manager.ex_training.models import Exercise


class ExerciseCreateView(LoginRequiredMixin, CreateView):
    model = Exercise
    form_class = ExerciseForm
    success_url = reverse_lazy('ex-training:list-exercise')


exercise_create_view = ExerciseCreateView.as_view()


class ExerciseUpdateView(LoginRequiredMixin, UpdateView):
    model = Exercise
    form_class = ExerciseForm
    success_url = reverse_lazy('ex-training:list-exercise')


exercise_update_view = ExerciseUpdateView.as_view()


class ExerciseListView(LoginRequiredMixin, ListView):
    model = Exercise
    context_object_name = 'exercise_list'
    paginate_by = 10


exercise_list_view = ExerciseListView.as_view()


class ExerciseDeleteView(LoginRequiredMixin, DeleteView):
    model = Exercise
    success_url = reverse_lazy('ex-training:list-exercise')


exercise_delete_view = ExerciseDeleteView.as_view()


class ExerciseDetailView(LoginRequiredMixin, DetailView):
    model = Exercise


exercise_detail_view = ExerciseDetailView.as_view()
