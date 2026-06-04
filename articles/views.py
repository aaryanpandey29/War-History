from .models import Articles
from django.views import generic


class IndexView(generic.ListView):
    template_name = "articles/index.html"
    model = Articles
    context_object_name = "latest_articles"


class DetailView(generic.DetailView):
    template_name = "articles/detail.html"
    context_object_name = "article"
    model = Articles
