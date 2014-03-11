from django.shortcuts import render, render_to_response

# Create your views here.
def dashboard(request):
    context = {'request': request, 'user': request.user}
    return render_to_response('acm_members/dashboard.html', context)