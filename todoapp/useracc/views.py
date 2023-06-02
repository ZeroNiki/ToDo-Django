from django.views import View
from django.shortcuts import render, redirect
from useracc.forms import UserCreationForm
from django.contrib.auth import authenticate, login

class Register(View):
    template_name = 'registration/register.html'

    def get(self, requests):
        context = {
            'form': UserCreationForm()
        }

        return render(requests, self.template_name, context)
    
    
    def post(self, requests):
        form = UserCreationForm(requests.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            passwd = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=passwd) 
            login(requests, user)
            return redirect('/')

        context = {
            'form' : form
        }
        
        return render(requests, self.template_name, context)
        
            
        