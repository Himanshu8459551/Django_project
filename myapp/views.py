from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from .models import Member1
from .forms import MemberForm

#Create your views here.
def image(request):
    template = loader.get_template('image.html')
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def all_member(request):
    member_list= Member1.objects.all().values()
    context ={
       'member_list':member_list
      }
    template = loader.get_template('all_member.html')
    return HttpResponse(template.render(context,request))

def detail(request, id):
    mymember = Member1.objects.get(id=id)
    template = loader.get_template('detail.html')
    context ={ 
        'mymember': mymember
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def new(request):
    if request.method =='POST':
        firstname =request.POST.get('firstname',)
        lastname =request.POST.get('lastname',)
        rollno =request.POST.get('rollno',)
        image = request.FILES['image']
        member=Member1(firstname=firstname,lastname=lastname,rollno=rollno)
        member.save()
    template = loader.get_template('new.html')
    return HttpResponse(template.render())

def update(request,id):
    member = Member1.objects.get(id=id)
    form = MemberForm(request.POST,instance=member)
    if form.is_valid():
        form.save()
        t1 = loader.get_template('new.html')
        return HttpResponse(t1.render())
    return render(request, 'update.html',{'form':form,'Member1':member})

@csrf_exempt
def delete(request,id):
    if request.method == 'POST':
        member = Member1.objects.get(id=id)
        member.delete()
        t1 = loader.get_template('all_member.html')
        return HttpResponse(t1.render())
    return render(request, 'delete.html')



