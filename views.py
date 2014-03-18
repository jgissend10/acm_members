from django.shortcuts import render, render_to_response

from archiver.decorators import dashboard_view
from archiver.models import ArchiverApp
# Create your views here.
@dashboard_view
def dashboard(request, context):
    context['members'] = ArchiverApp.objects.get(app_label='acm_members').members.all()
    return render_to_response('acm_members/dashboard.html', context)
