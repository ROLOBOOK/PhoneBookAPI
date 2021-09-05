from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrganizationViewSet, SearchViewSet


router = DefaultRouter()
router.register('search', SearchViewSet)
router.register('', OrganizationViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]
