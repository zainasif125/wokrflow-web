from django.shortcuts import redirect
from django.urls import reverse_lazy


def index(request):
    return redirect(reverse_lazy('login'))
def index2(request):
    return redirect(reverse_lazy('logout'))
