from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = CustomUserForm()
    return render(request, 'register.html', {'form': form})
