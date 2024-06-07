from django.shortcuts import render
from django import forms


class NewForm(forms.Form):
    name = forms.CharField(max_length=50, label='Your Name', widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(label='Your Email',widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    message = forms.CharField( label='Your Message', widget=forms.Textarea(attrs={'placeholder': 'Message'}))

# Create your views here.
def newform(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(form.cleaned_data)
            return render(request, 'newform/success.html', {"name":name})
    else:
        form = NewForm()

    return render(request, 'newform/newform.html', {
        'form': form
    })