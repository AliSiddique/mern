from django_filters import rest_framework as filters
from .models import Listing

class ListingFilter(filters.FilterSet):
    keywords = filters.CharFilter(field_name='title',lookup_expr='icontains')
    min_bedrooms = filters.NumberFilter(field_name='bedrooms' or 0, lookup_expr="gte")
    max_bedrooms = filters.NumberFilter(field_name='bedrooms' or 6, lookup_expr="lte")
    min_bathrooms = filters.NumberFilter(field_name='bathrooms' or 0, lookup_expr="gte")
    max_bathrooms = filters.NumberFilter(field_name='bathrooms' or 6, lookup_expr="lte")
    min_price = filters.NumberFilter(field_name='price' or 0, lookup_expr="gte")
    max_price = filters.NumberFilter(field_name='price' or 100000, lookup_expr="lte")
    location = filters.CharFilter(field_name='location',lookup_expr='icontains')
    ordering = filters.OrderingFilter(
        fields=(
            ('price', 'price'),
            ('created_at', 'created_at')
        )
    )
    class Meta:
        model = Listing
        fields = ['keywords','min_bedrooms','max_bedrooms','min_bathrooms','max_bathrooms','min_price','max_price','location','ordering']