# Create your views here.
from django.views.generic import TemplateView


class RangeHitsView(TemplateView):
    template_name = 'golf/range_hits.html'


range_hits_view = RangeHitsView.as_view()
