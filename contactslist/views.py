from django.shortcuts import render, redirect
from .models import User
from django.template import loader
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def post_list(request):
    person = User.objects.all()
    context={'person': person}
    return render(request, 'blog/Mainpage.html', context)
def post_list_user(request, id):
    user = User.objects.get(id=id)
    person = User.objects.all()
    context = {'person': person , 'user' :user}
    return render(request, 'blog/MainpageLogin.html',context)
def signup(request):
    return render(request, 'blog/signup.html')

def create(request):
    print(request.POST)
    person = User(u_id=request.POST['ID'], e_mail=request.POST['e_mail'],password=request.POST['password'],
                  phone_number=request.POST['phone_number'])

    person.save()
    return redirect('/signin')

def gotosignin(request):
    return render(request,'blog/signin.html')
def signinuser(request):
    id = request.POST['ID']
    password = request.POST['password']
    person = User.objects.all()
    print(type(person))
    for cursor in person:
        if cursor.u_id == id:
            if cursor.password == password:
                return redirect('/'+str(cursor.id))
            else:
                messages.info(request,"password is wrong")
                return redirect('/signin')
    messages.info(request,"no ID exist")
    return redirect('/signin')

def edit(request, id):
    person = User.objects.get(id=id)
    context = {'person': person}
    return render(request, 'blog/UserinfoEdit.html',context)

def update(request, id):
    person = User.objects.get(id=id)
    person.ID = request.POST['ID']
    person.e_mail = request.POST['e_mail']
    person.phone_number = request.POST['phone_number']
    person.save()
    return redirect('/')

def destroy(request, id):
    people = User.objects.get(id=id)
    people.delete()
    return redirect('/')

def search(request):
    searchName = request.GET.get('name','')
    if searchName != "":
        return search_specific(request, searchName)
    template = loader.get_template('blog/Usersearch.html')
    contacts = User.objects.order_by('pk')
    context = {
        'contacts' : contacts,
    }
    return HttpResponse(template.render(context, request))

def search_specific(request, name):
    searched = User.objects.filter(name__icontains=name)
    context = {
        'name' : name,
        'contacts' : searched,
    }
    template = loader.get_template('blog/UserResult.html')
    return HttpResponse(template.render(context, request))
