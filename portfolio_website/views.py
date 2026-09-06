from django.contrib import messages
from django.shortcuts import render , redirect
from django.http import Http404
from django.contrib.auth import login , logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required , permission_required 
from .models import skill , projects , contact , experience
from .form import ContactForm, LoginForm
from django.views.generic import ListView , DetailView 

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
def home_view(request):
    context={
        "skills": skill.objects.all(),
        'projects': projects.objects.all(),
        'experiences': experience.objects.all(),
        'contacts': contact.objects.all()
    }
    return render(request , "home.html" , context)

def tester(request):
    return render(request , 'tester.html')



def project_detail(request, project_slug):
    """Render the selected featured project and its full case-study details."""
    project_data = {
        'student-management-system': {
            'number': '01',
            'title': 'Student Management System',
            'tagline': 'A structured academic platform for managing students, courses and records.',
            'description': 'A complete web-based system that brings student information, departments, courses and academic records into one secure workspace. It helps administrators keep academic data organized and easy to manage.',
            'stack': ['Django', 'MySQL', 'HTML', 'CSS'],
            'features': ['Secure authentication and role-based access', 'Student, department and course management', 'Create, update and delete academic records', 'Organized dashboard for day-to-day administration'],
        },
        'invoice-management-system': {
            'number': '02',
            'title': 'Invoice Management System',
            'tagline': 'A practical billing workspace for creating and organizing customer invoices.',
            'description': 'A business-oriented application that makes invoice creation and record keeping simpler. Customer billing data is kept in one place so invoices can be managed accurately and efficiently.',
            'stack': ['Django', 'MySQL', 'Bootstrap'],
            'features': ['Customer and billing record management', 'Create and organize invoices', 'Clear invoice history for easier tracking', 'Responsive interface for everyday business use'],
        },
        'hospital-management-system': {
            'number': '03',
            'title': 'Hospital Management System',
            'tagline': 'A centralized healthcare platform for patients, doctors and appointments.',
            'description': 'A structured hospital management application designed to coordinate patient information, doctor profiles, appointments and medical records through a reliable backend system.',
            'stack': ['Django', 'Python', 'MySQL'],
            'features': ['Patient and doctor profile management', 'Appointment scheduling workflow', 'Structured medical record handling', 'Secure, organized healthcare data'],
        },
        'ai-interior-design-system': {
            'number': '04',
            'title': 'AI Interior Design System',
            'tagline': 'An AI-powered concept for smarter room design ideas.',
            'description': 'An application concept that analyzes room details and helps users explore interior design ideas with intelligent processing. The goal is to turn early design decisions into a more guided experience.',
            'stack': ['Python', 'AI', 'Django'],
            'features': ['Room analysis input workflow', 'Intelligent interior design suggestions', 'Django-powered application structure', 'Scalable foundation for AI features'],
        },
    }
    project = project_data.get(project_slug)
    if project is None:
        raise Http404('Project not found')
    return render(request, 'project_detail.html', {'project': project})


# Create your views here.
