from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
            # Perform necessary processing or call the next step in the pipeline
            return redirect('jobtracker:job_list')
    else:
        form = DocumentForm()
    return render(request, 'upload/upload_document.html', {'form': form})
