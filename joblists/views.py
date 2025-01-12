from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'joblists/index.html')
def joblist(request, job_id):
    context = {
        'job_id': job_id
    }
    return render(request, 'joblists/joblist.html', context)