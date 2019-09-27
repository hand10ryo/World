import os
import random

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template.context_processors import csrf
from django.urls import reverse


def index(request):
    return render(request, 'worldapp/index.html', {})

# Create your views here.
