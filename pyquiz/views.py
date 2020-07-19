from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def profile(request):
    return render(request, 'profile_side.html', {'user': request.user})
