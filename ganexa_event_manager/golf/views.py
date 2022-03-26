# Create your views here.
from django.views.generic import TemplateView

from ganexa_event_manager.golf.models import GolfClub


class RangeHitsView(TemplateView):
    template_name = 'golf/range_hits.html'

    def get_context_data(self, **kwargs):
        player = self.request.user
        ctx = super(RangeHitsView, self).get_context_data(**kwargs)
        ctx['golf_clubs'] = GolfClub.objects.filter(player=player)

        return ctx


range_hits_view = RangeHitsView.as_view()
