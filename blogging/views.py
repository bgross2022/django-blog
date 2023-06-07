from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class BloggingListView(ListView):
    template_name = "blogging/list.html"

    def get_queryset(self):
        self.published = Post.objects.exclude(published_date__exact=None)
        return self.published.order_by("-published_date")


class BloggingDetailView(DetailView):
    template_name = "blogging/detail.html"

    def get_queryset(self):
        return Post.objects.exclude(published_date__exact=None)
