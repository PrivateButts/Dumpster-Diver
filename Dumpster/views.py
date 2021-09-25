from django.shortcuts import render
from django.views import generic
import django_filters
from django_filters.views import FilterView

from .models import Asset, Tag


class AssetFilter(django_filters.FilterSet):
    class Meta:
        model = Asset
        fields = {
            'name': ['exact', 'contains'],
            'type': ['exact'],
            'tags': ['exact']
        }
        # fields = ['name', 'tags']


class AssetListView(FilterView):
    context_object_name = "Assets"
    model = Asset
    template_name = "Dumpster/asset_list.html"
    filterset_class = AssetFilter
    paginate_by = 100


class AssetDetailView(generic.DetailView):
    context_object_name = "Asset"
    model = Asset
