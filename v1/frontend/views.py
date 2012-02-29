from django.shortcuts import render_to_response

def base(request):
    return render_to_response('base.html')

def home(request):
    return render_to_response('home.html')

def createsurvey(request):
    return render_to_response('createsurvey.html')

def preview(request):
    return render_to_response('preview.html')

def dashboard(request):
    return render_to_response('dashboard.html')

