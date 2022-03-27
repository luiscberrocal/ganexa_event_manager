# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView

from .forms import RangeHitForm
from .models import GolfClub, RangeHit, GolfCourse


class RangeHitsView(TemplateView):
    template_name = 'golf/range_hits.html'

    def get_context_data(self, **kwargs):
        player = self.request.user
        ctx = super(RangeHitsView, self).get_context_data(**kwargs)
        ctx['golf_clubs'] = GolfClub.objects.filter(player=player)
        ctx['directions'] = RangeHit.DIRECTION_CHOICES

        return ctx


range_hits_view = RangeHitsView.as_view()


@login_required
def save_hit_view(request):
    form_dict = request.POST.copy()
    form_dict['player'] = request.user
    form_dict['course'] = GolfCourse.objects.first()
    print(f'>> hit dictionary {form_dict}')
    form = RangeHitForm(data=form_dict)
    if form.is_valid():
        form.save()
    else:
        print(form.errors)
    template_name = 'golf/partials/stats.html'
    today = timezone.now().date()
    qs = RangeHit.objects.filter(player=request.user, created__startswith=today)
    context = {'hits': qs[:10], 'hit_count': qs.count()}
    response = render(request, template_name, context)
    return response


@login_required
def list_player_hits_view(request):
    template_name = 'golf/partials/stats.html'
    today = timezone.now().date()
    qs = RangeHit.objects.filter(player=request.user, created__startswith=today)
    context = {'hits': qs[:10], 'hit_count': qs.count()}
    response = render(request, template_name, context)
    return response


@require_http_methods(['DELETE'])
@login_required
def delete_range_hit(request, pk):
    try:
        range_hit = RangeHit.objects.get(pk=pk)
        if range_hit.player == request.user:
            range_hit.delete()
    except RangeHit.DoesNotExist:
        pass
    return list_player_hits_view(request)
