from django.shortcuts import render, render_to_response

from archiver.decorators import dashboard_view
from archiver.models import ArchiverApp
# Create your views here.
@dashboard_view('acm_members')
def dashboard(request, context):
    return render_to_response('acm_members/dashboard.html', context)
