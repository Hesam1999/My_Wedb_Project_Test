from multiprocessing import context
from re import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = Members(firstname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
            'mymember' : mymember,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('index'))
"""
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'firstname': 'Linus',
  }
  
  return HttpResponse(template.render(context, request))    

def testing(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
# part 10 Training
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'greeting' : 1,
  }
  return HttpResponse(template.render(context,request))

def testing(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers' : mymembers,
  }
  return HttpResponse(template.render(context,request))

# part 11 Training
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'greeting' : 1,
  }
  return HttpResponse(template.render(context,request))

#Part 11 Traning step 10 and step 11 and step 12
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'greeting' : 5,
    'day' : 'Friday',
  }
  return HttpResponse(template.render(context,request))

#Part 11 Traning step 13 and step 14 
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'], 
  }
  return HttpResponse(template.render(context,request))

"""
"""
Part 11 Traning step 15 and step 16 and step 17 and step 18
Work with conditions

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'x': ['Apple', 'Banana', 'Cherry'], 
    'y': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context,request))
"""
"""
# Part 12 Training 
# step 1
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],     
  }
  return HttpResponse(template.render(context, request))
"""
