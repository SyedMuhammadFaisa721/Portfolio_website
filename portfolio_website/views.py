from django.contrib import messages
from django.shortcuts import render , redirect
from django.http import Http404
from django.contrib.auth import login , logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required , permission_required 
from .models import skill , projects , contact , experience , projectimage
from .form import ContactForm, LoginForm
from django.views.generic import ListView , DetailView 
from django.http import FileResponse
from django.contrib.staticfiles import finders

def log_in(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request , user)
            return redirect("home")
    else:
        form = LoginForm()
    return render(request , 'log_in.html' , {'form': form})

def home(request):
    return render(request , 'home.html')
def contact_view(request):
    if request.method =="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    data ={
        'form':form
    }
    return render(request , 'contact.html' , data)
def home_view(request ):
    context={
        "skills": skill.objects.all(),
        'projects': projects.objects.all(),
        'experiences': experience.objects.all(),
        'contacts': contact.objects.all()
    }
    return render(request , "home.html" , context)

def tester(request):
    return render(request , 'delete.html')


def download_cv(request):
    file_path = finders.find('cv/Syed_Muhammad_Faisal_Resume_WithPhoto.pdf')
    return FileResponse(
        open(file_path , 'rb'),
        as_attachment=True,
        filename="Syed_Muhammad_Faisal_Resume_WithPhoto.pdf"
    )
class ProjectDetailView(DetailView):
    model = projects
    template_name = 'tester.html'
    context_object_name = 'projectdetails'


# Create your views here.
