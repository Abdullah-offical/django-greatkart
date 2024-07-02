from django.shortcuts import render

def carts(request):
    return render(request, 'store/carts.html')