from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.decorators.http import require_http_methods
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView, TemplateView
import plotly.express as px
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

    def get_form_kwargs(self):
        kwargs = super(FastingSessionUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


fasting_session_update_view = FastingSessionUpdateView.as_view()


class FastingSessionListView(LoginRequiredMixin, ListView):
    model = FastingSession
    context_object_name = 'fasting_session_list'
    paginate_by = 5

    def get_queryset(self):
        qs = super(FastingSessionListView, self).get_queryset()
        return qs.filter(user=self.request.user)


fasting_session_list_view = FastingSessionListView.as_view()


class FastingSessionDeleteView(LoginRequiredMixin, DeleteView):
    model = FastingSession
    success_url = reverse_lazy('fasting-track:list-fasting-session')


fasting_session_delete_view = FastingSessionDeleteView.as_view()


class FastingSessionDetailView(LoginRequiredMixin, DetailView):
    model = FastingSession


fasting_session_detail_view = FastingSessionDetailView.as_view()


@login_required
def finish_fast(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        fasting_session = FastingSession.objects.get(user=request.user, id=pk)
        fasting_session.finish()
        url = reverse('fasting_track:detail-fasting-session', kwargs={'pk': fasting_session.pk})
        response = redirect(url)
        return response
    except FastingSession.DoesNotExist:
        pass


@require_http_methods(['GET'])
@login_required
def statistics_view(request: HttpRequest) -> HttpResponse:
    average_duration = FastingSession.objects.average_hours(user=request.user)
    context = {'average_duration': average_duration,
               'longest_fasting_session': FastingSession.objects.longest_fasting_session(user=request.user)}
    template_name = 'fasting_track/partials/statistics.html'
    response = render(request, template_name, context)
    return response

@require_http_methods(['GET'])
@login_required
def bar_chart_view(request: HttpRequest) -> HttpResponse:
    context = dict()
    qs = FastingSession.objects.filter(user=request.user)[:7]
    import time
    start = time.time()
    fig = px.bar(
        x=[fs.start_date for fs in qs],
        y=[fs.duration for fs in qs]
    )
    context['building_chart'] = time.time() - start
    start = time.time()
    chart = fig.to_html(full_html=False) #, include_plotlyjs=False)
    context['building_chart_to_html'] = time.time() - start
    context['chart'] = chart
    template_name = 'fasting_track/partials/bar_chart.html'

    response = render(request, template_name, context)
    return response
