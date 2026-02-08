from django.shortcuts import render

# Create your views here.
def qrGen(request):
    return render(request, 'qrGen/qrGen.html')
