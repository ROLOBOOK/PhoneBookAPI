from rest_framework import filters
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Organization
from .serializers import OrganizationNameSerializer, OrganizationFullSerializer
from .paginator_ import LargeResultsSetPagination


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationNameSerializer
    pagination_class = PageNumberPagination


class SearchViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationFullSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'employees__full_name', 'employees__phone_numbers__phone_number', ]
