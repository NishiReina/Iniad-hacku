from django.shortcuts import render

# Create your views here.
def top(request):
    return render(request, 'TotalWeb/top.html')
def test(request):
    return render(request, 'TotalWeb/test.html')
