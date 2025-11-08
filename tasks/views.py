from django.shortcuts import render

def index(request):
    return render(request,'index.html',context={'title': 'To_Do Manager'})
