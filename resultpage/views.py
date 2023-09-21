from django.shortcuts import render
from .models import CompletedJob

def completed_job_list(request):
    completed_jobs = CompletedJob.objects.all()
    return render(request, 'resultpage/completed_job_list.html', {'completed_jobs': completed_jobs})

def download_result(request, completed_job_id):
    completed_job = CompletedJob.objects.get(id=completed_job_id)
    # Implement the logic to serve the file for download
    return ...