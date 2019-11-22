from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList
from .forms import CreateListForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
def test_response(request):
    return HttpResponse('tu bedzie pierwsza strona z paskiem')


def home_response(request):
    return render(request, 'login.html')

@login_required(redirect_field_name='')
def after_login_response(request):
    return render(request, 'home.html')





def index(response, id):
    ls = ToDoList.objects.get(id=id)
    if response.user.todolist.all():
        if response.method == "POST":
            if response.POST.get('save'):
                for item in ls.item_set.all():
                    if response.POST.get("c"+str(item.id))=="clicked":
                        item.complete=True
                    else:
                        item.complete=False
                    item.save()
            elif response.POST.get('newItem'):
                txt=response.POST.get("new")
                if len(txt)>2:
                    ls.item_set.create(text=txt,complete=False)
                else:
                    print('invalid')
        return render(response,'list.html',{"ls":ls})
    else:
        return render(response,'view.html',{})


def home(response):
    return render(response, "home.html", {})





@login_required
def create(response):
    if response.method == "POST":
        form =CreateListForm(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t=ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)


        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateListForm()

    return render(response, "create.html", {"form":form})


def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if ls in response.user.todolist.all():

        if response.method == "POST":
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")

        return render(response, "list.html", {"ls":ls})

    return render(response, "home.html", {})

@login_required
def view(request):
    l = ToDoList.objects.all()
    return render(request, "view.html", {"lists": l})

@login_required
def view(response):
    return render(response, "view.html", {})