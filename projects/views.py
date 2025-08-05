from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.forms import ModelForm
from projects.models import Project
  
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']
 
@require_http_methods(["GET"])
def project_index(request, template_name='projects/project_index.html'):
    projects = Project.objects.all()
    data = {}
    data['projects'] = projects
    return render(request, template_name, data)
 
@require_http_methods(["GET"])
def project_create(request, template_name='projects/project_create.html'):
    data = {}
    return render(request, template_name, data)
 
@require_http_methods(["POST"])
def project_store(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Project saved successfully!')
 
    return redirect('project_index')
 
@require_http_methods(["GET"])
def project_show(request, pk, template_name='projects/project_show.html'):
    project= get_object_or_404(Project, pk=pk)
    return render(request, template_name, {'project':project})
 
@require_http_methods(["GET"])
def project_edit(request, pk, template_name='projects/project_edit.html'):
    project= get_object_or_404(Project, pk=pk)
    form = ProjectForm(request.POST or None, instance=project)
    return render(request, template_name, {'form':form, 'project':project})
 
@require_http_methods(["POST"])
def project_update(request, pk):
    project= get_object_or_404(Project, pk=pk)
    form = ProjectForm(request.POST or None, instance=project)
    method = request.POST.get('_method', '')
    if form.is_valid():
        if method=='PUT':
            form.save()
            messages.success(request, 'Project updated successfully!')
    return redirect('project_index')
 
@require_http_methods(["POST"])
def project_delete(request, pk):
    project= get_object_or_404(Project, pk=pk)    
    method = request.POST.get('_method', '')
    if method=='DELETE':
        project.delete()
        messages.success(request, 'Project deleted successfully!')
    return redirect('project_index')
