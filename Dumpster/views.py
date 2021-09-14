from django.shortcuts import render
from django.views import generic

from .models import Asset


class AssetDetailView(generic.DetailView):
    context_object_name = "Asset"
    model = Asset