from django.urls import include, path, re_path
from django.views.generic import ListView, DetailView
from sportnews.models import Articles

urlpatterns = [
    path('', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20], template_name="sportnews/posts.html")),
    re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model = Articles, template_name = "sportnews/post.html"))
]
