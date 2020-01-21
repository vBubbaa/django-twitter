from django.shortcuts import render

def UserIndex(request):
    return render(request, 'UserIndex.html')
