from django.shortcuts import render
from django.http import HttpResponse
from splash.forms import PhotographerForm, PlannerForm
from django.shortcuts import render_to_response

def index(request):
    return render(request, 'splash/index.html')

def about(request):
    return render(request, 'splash/about.html')

def planners(request):
    return render(request, 'splash/planners.html')

def photographers(request):
    form = PhotographerForm()
    if request.method == 'POST':
        form = PhotographerForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print(form.errors)
    return render(request, 'splash/photographers.html', {'form': form})

def planners(request):
    form = PlannerForm()
    if request.method == 'POST':
        form = PlannerForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print(form.errors)
    return render(request, 'splash/planners.html', {'form': form})

def index_lp(request):
    return render(request, 'splash/index_lp.html')
