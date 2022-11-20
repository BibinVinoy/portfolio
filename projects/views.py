from django.shortcuts import render
from projects.models import project
# Create your views here.
def project_index(request):
    projects = project.objects.all()
    context = {
        'projects':projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project_data = project.objects.get(id=pk)
    context = {
        "project":project_data
    }
    return render(request, "project_detail.html", context)