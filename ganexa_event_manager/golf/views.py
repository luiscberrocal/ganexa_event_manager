# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import GolfClub, RangeHit


class RangeHitsView(TemplateView):
    template_name = 'golf/range_hits.html'

    def get_context_data(self, **kwargs):
        player = self.request.user
        ctx = super(RangeHitsView, self).get_context_data(**kwargs)
        ctx['golf_clubs'] = GolfClub.objects.filter(player=player)
        ctx['directions'] = RangeHit.DIRECTION_CHOICES

        return ctx


@login_required
def save_hit_view(request):
    print(request.POST)
    template_name = 'golf/partials/stats.html'
    context = {'hits': RangeHit.objects.all()[:10]}
    response = render(request, template_name, context)
    return response


range_hits_view = RangeHitsView.as_view()
