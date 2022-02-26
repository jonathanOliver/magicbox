from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login in the user
            return redirect('articles:list')
    else:
        form = AuthenticationForm()

    return render(request, 'magicBox/login.html', {'form':form})



def dashboard_view(request):
    return render(request, 'magicBox/dashboard.html')



def sidebar_view(request):
    return render(request, 'magicBox/sidebar.html')