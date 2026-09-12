from django.contrib import messages
from django.shortcuts import render , redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth import login , logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required , permission_required 
from .models import skill , projects , contact , experience , projectimage , testemonial
from .form import ContactForm, LoginForm
from django.views.generic import ListView , DetailView 
from django.http import FileResponse
from django.contrib.staticfiles import finders
from django.core.paginator import Paginator

def log_in(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request , user)
            return redirect("dashboard")
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
        'projects': projects.objects.all().order_by('-project_serial_number')[:4],
        'experiences': experience.objects.all(),
        'contacts': contact.objects.all(),
        'testemonial': testemonial.objects.all(),
    }
    return render(request , "home.html" , context)

def all_project(request):
     project = projects.objects.all()

     paginator = Paginator(project , 8)
     page_number = request.GET.get('page')
     page_obj = paginator.get_page(page_number)
     context = {
        'page_obj': page_obj,
        'project':  project


     }   
     return render(request , 'projects.html' , context )


@login_required(login_url='login')
def dashboard_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        contact_id = request.POST.get('contact_id')
        message_obj = get_object_or_404(contact, id=contact_id)

        if action == 'toggle_read':
            message_obj.is_read = not message_obj.is_read
            message_obj.save(update_fields=['is_read'])
            status = 'read' if message_obj.is_read else 'unread'
            messages.success(request, f'Message marked as {status}.')
        elif action == 'delete':
            message_obj.delete()
            messages.success(request, 'Message deleted successfully.')

        return redirect('dashboard')

    all_contacts = contact.objects.all().order_by('-created_at', '-id')
    unread_contacts = all_contacts.filter(is_read=False)

    context = {
        'contacts': all_contacts,
        'total_count': all_contacts.count(),
        'unread_count': unread_contacts.count(),
        'read_count': all_contacts.count() - unread_contacts.count(),
    }
    return render(request, 'dashboard.html', context)


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
def tester(request):
    return render(request , 'tester.html')


# Create your views here.
