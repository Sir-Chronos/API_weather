from django.views.generic import TemplateView

class WeatherView(TemplateView):
    template_name = "index.html"
