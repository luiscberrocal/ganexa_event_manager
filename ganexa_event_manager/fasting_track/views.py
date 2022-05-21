from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView, TemplateView

from .forms import FastingSessionForm
from .models import FastingSession


class FastingSessionMainView(TemplateView):
    template_name = 'fasting_track/fasting_track_index.html'


fasting_session_main_view = FastingSessionMainView.as_view()


class FastingSessionCreateView(LoginRequiredMixin, CreateView):
    model = FastingSession
    form_class = FastingSessionForm
    success_url = reverse_lazy('fasting-track:list-fasting-session')

    def get_form_kwargs(self):
        kwargs = super(FastingSessionCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs



fasting_session_create_view = FastingSessionCreateView.as_view()


class FastingSessionUpdateView(LoginRequiredMixin, UpdateView):
    model = FastingSession
    form_class = FastingSessionForm
    success_url = reverse_lazy('fasting-track:list-fasting-session')


fasting_session_update_view = FastingSessionUpdateView.as_view()


class FastingSessionListView(LoginRequiredMixin, ListView):
    model = FastingSession
    context_object_name = 'fasting_session_list'
    paginate_by = 10


fasting_session_list_view = FastingSessionListView.as_view()


class FastingSessionDeleteView(LoginRequiredMixin, DeleteView):
    model = FastingSession
    success_url = reverse_lazy('fasting-track:list-fasting-session')


fasting_session_delete_view = FastingSessionDeleteView.as_view()


class FastingSessionDetailView(LoginRequiredMixin, DetailView):
    model = FastingSession


fasting_session_detail_view = FastingSessionDetailView.as_view()


def advance(request, pk):
    session = FastingSession.objects.get(id=pk)
    p_advance = session.current_duration / session.target_duration
    ctx = {'current_advance': p_advance}
    template = 'fasting_track/partials/advance.html'
    response = render(request, template, ctx)
    return response

