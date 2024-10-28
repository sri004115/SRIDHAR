from django.shortcuts import render, redirect
from .forms import SurveyForm

def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('survey_success')
    else:
        form = SurveyForm()
    return render(request, 'survey/survey_form.html', {'form': form})

def survey_success(request):
    return render(request, 'survey/survey_success.html')

from django.shortcuts import render

def home(request):
    return render(request, 'survey/home.html')

