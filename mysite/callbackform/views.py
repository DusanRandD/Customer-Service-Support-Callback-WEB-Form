from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import CallbackFormForm
from .models import CallbackForm

# Create your views here.

def display_callback_form(request):
    if request.method=='POST':
        form = CallbackFormForm(request.POST)
        if form.is_valid():
            CallbackForm.objects.create(name=request.POST['name'],
                                       phone_number=request.POST['phone_number'],
                                       company=request.POST['company'],
                                       email=request.POST['email'],
                                       subject=request.POST['subject'],
                                       problem_description=request.POST['problem_description'],
                                       support_datetime=request.POST['support_datetime']
                                       )
            return render(request, 'callbackform/confirmation.html', {})
        else:
            return render(request, 'callbackform/contact_form.html', {'form': form})
    else:
        form = CallbackFormForm()
        return render(request,'callbackform/contact_form.html',{'form':form})

def display_confirmation(request):
    return render(request,'calbackform/confirmation.html',{})

