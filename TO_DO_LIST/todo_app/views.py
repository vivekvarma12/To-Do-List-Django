from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import todo_List


def to_do(request):
    if request.method == "POST":
        value = request.POST['element']
        if (value != "") and (not todo_List.objects.filter(desc=value).exists()):
            obj = todo_List(desc=value)
            obj.save()
            s = todo_List.objects.all()
            return render(request, 'Homed.html', {'cont': s})
        else:
            messages.info(request, 'Task already exists!!')
            s = todo_List.objects.all()
            return render(request, 'Homed.html', {'cont': s})
    else:
        s = todo_List.objects.all()
        return render(request, 'Homed.html', {'cont': s})

def delete(request, id1):
    d = todo_List.objects.get(id=id1)
    d.delete()
    return HttpResponseRedirect('/to_do')

def edit(request, id2):
    e = todo_List.objects.get(id=id2)
    e.desc = request.POST['element1']
    e.save()
    return HttpResponseRedirect('/to_do')
