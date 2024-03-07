from django.shortcuts import render
from .models import formvalidation
from .forms import formvalidationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.
def form_view(request):
    if request.method == 'POST':
        form=formvalidationForm(request.POST)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.save()

    else:
        form=formvalidationForm
    return render(request,'form_app/form.html',{'form':form})


def display_data(request):
    form_data = formvalidation.objects.all()
    return render(request, 'display.html', {'form_data': form_data})


def mylogin(LoginView):
    template_name=""
    success_url=reverse_crazy("")





