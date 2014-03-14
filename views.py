from django.shortcuts import render, render_to_response

from archiver.decorators import dashboard_view
# Create your views here.
@dashboard_view
def dashboard(request, context):
    return render_to_response('acm_members/dashboard.html', context)
