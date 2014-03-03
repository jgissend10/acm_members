from django.conf.urls import url, patterns, include
from rest_framework import viewsets, routers

from acm_members.models import Member

# ViewSets define the view behavior.
class MemberViewSet(viewsets.ModelViewSet):
    model = Member

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'members', MemberViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
