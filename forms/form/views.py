from datetime import datetime

from django.core.validators import RegexValidator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms

# Create your views here.

# class MyForm(forms.Form):
#     name = forms.CharField(max_length=30, label='Name',widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
#     age = forms.IntegerField(required=False, label='Age')
#     gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], label='Gender')
#     birthday = forms.DateField( required=False, label='Birthday')
#     address = forms.CharField(max_length=100, label='Address')
#     city = forms.CharField(max_length=30, label='City')
#     state = forms.CharField(max_length=30, label='State')
#     country = forms.CharField(max_length=30, label='Country')
#     phone = forms.CharField(max_length=10, validators=
#     [RegexValidator(r'^\+?1?\d{9,13}$',
#                     message="Phone number must be entered in the format '+123456789'. "
#                             "Up to 15 digits "
#                             "allowed.")], label='Phone')


class MyForm(forms.Form):
    name = forms.CharField(max_length=30, label='Full Name',widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    age = forms.IntegerField(required=False, label='Ur Age')
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], label='Gender')
    birthday = forms.DateField( required=False, label='DOB')
    address = forms.CharField(max_length=100, label='Address')


def form(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            birthday = form.cleaned_data['birthday']
            address = form.cleaned_data['address']
            # city = form.cleaned_data['city']
            # state = form.cleaned_data['state']
            # country = form.cleaned_data['country']
            # phone = form.cleaned_data['phone']
            print(name, age, gender, birthday, address)
            # print(city, state, country, phone)
            return render(request, 'form/success.html', {'name': name})
            # return HttpResponseRedirect('form/success.html')
    else:
        form = MyForm()
    return render(request, 'form/form.html', {
        'form':form
    })
