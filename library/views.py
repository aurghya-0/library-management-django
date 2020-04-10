from django.shortcuts import render


def library_home(request):
    return render(request, 'library/library_home.html')
