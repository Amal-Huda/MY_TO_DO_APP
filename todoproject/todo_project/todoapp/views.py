from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import task
from .forms import updateform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create class views
class tasklistview(ListView):
    model = task
    template_name = 'Home.html'
    context_object_name ='tasklist'


class taskdetailview(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'task'
class taskupdateview(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'task'
    fields=('taskname','taskpriority','taskdate')
    def get_success_url(self):

        return reverse_lazy('detail',kwargs={'pk':self.object.id})
class taskdelete(DetailView):
    model = task
    template_name = 'delete.html'
    success_url=reverse_lazy('home')




# Create your views here.
def demo(request):
    # return HttpResponse("Todo app")
    tasklist=task.objects.all()
    if request.method=='POST':
        taskname=request.POST.get('task','')
        taskpriority=request.POST.get('priority','')
        taskdate=request.POST.get('date','')
        mytask=task(taskname=taskname,taskpriority=taskpriority,taskdate=taskdate)
        mytask.save()

    return render(request,'Home.html',{'tasklist':tasklist})
def delete(request,taskid):

        deletetask=task.objects.get(id=taskid)
        if request.method == 'POST':
            deletetask.delete()
            return redirect('/')
        return render(request,'delete.html')
def update_task(request,tid):
    updatetask=task.objects.get(id=tid)
    fupdate=updateform(request.POST or None,instance=updatetask)
    if request.method=='POST':
        if fupdate.is_valid():
            fupdate.save()
            return redirect('/')
    return render(request,'Edit.html',{'uform':fupdate,'utask':updatetask})

