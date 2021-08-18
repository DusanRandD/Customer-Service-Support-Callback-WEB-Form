from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import CallbackFormForm
from .models import CallbackForm

# Create your views here.

def display_callback_form(request):
    # if user enter information in form
    if request.method=='POST':
        form = CallbackFormForm(request.POST)
        # if entered values are good pass it to database
        if form.is_valid():
            CallbackForm.objects.create(name=request.POST['name'],
                                       phone_number=request.POST['phone_number'],
                                       company=request.POST['company'],
                                       email=request.POST['email'],
                                       subject=request.POST['subject'],
                                       problem_description=request.POST['problem_description'],
                                       support_datetime=request.POST['support_datetime']
                                       )
            # Send user confirmation
            return render(request, 'callbackform/confirmation.html', {})
        # If enteries are bad go back to form page that user continue to edit
        else:
            return render(request, 'callbackform/contact_form.html', {'form': form})
    # If user first time load page sent empty form
    else:
        form = CallbackFormForm()
        return render(request,'callbackform/contact_form.html',{'form':form})

def display_confirmation(request):
    return render(request,'calbackform/confirmation.html',{})

