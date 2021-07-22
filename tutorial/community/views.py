from django.shortcuts import render
from community.forms import *

# Create your views here.
def write(request):
    form = Form()
    return render(request, 'write.html')
