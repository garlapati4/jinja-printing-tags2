from django.shortcuts import render

# Create your views here.
def amma(request):
    d={'name':'Kalavathi'}
    return render(request,'amma.html',context=d)
