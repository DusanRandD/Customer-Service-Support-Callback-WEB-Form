from django import forms

class CallbackFormForm(forms.Form):
    name = forms.CharField(label='Name',max_length=40,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(label='Phone number',max_length=40,required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    company = forms.CharField(label='Company',max_length=80,required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='email',required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    subject = forms.CharField(label='Subject',max_length=240,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    problem_description = forms.CharField(label='Problem description',max_length=2000,required=True,widget=forms.Textarea(attrs={'class':'form-control'}))
    support_datetime = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M'])