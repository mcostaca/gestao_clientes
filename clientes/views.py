from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import personForm

# Create your views here.

@login_required
def create(request):
    form = personForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('query_user')
    
    return render(request, 'temp/create.html',{'form':form})

@login_required
def home(request):
    lists = Person.objects.all()
    return render(request, 'temp/home.html', {'qr':lists})

@login_required
def update(request, id):
    query = Person.objects.get(pk=id)
    user_form = personForm(request.POST or None, instance=query)
    if user_form.is_valid():
        user_form.save()
        return redirect('query_user')
    return render(request, 'temp/update.html',{'user':user_form})

@login_required
def delete(request, id):
    Person.objects.filter(pk=id).delete()
    return redirect('query_user')


