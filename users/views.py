from django.shortcuts import render ,redirect 
from django.urls import reverse_lazy
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.admin.models import LogEntry, ADDITION
# Render to PDF
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

def render_to_pdf(template_src,context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    return None

data = {
    'naissance' : Naissance.objects.first(),

}

class ViewPDF(View):
    def get(self,request,*args,**kwargs):
        pdf = render_to_pdf('users/model.html',data)
        return HttpResponse(pdf,content_type="application/pdf")

class DownloadPDF(View):
    def get(self,request,*args,**kwargs):
        pdf = render_to_pdf('users/model.html',data)
        response = HttpResponse(pdf,content_type="application/pdf")
        filename = "ActeNaissance_%s.pdf" %("1111112")
        content = "attachment; filename=%s" %(filename)
        response['Content-Disposition'] = content
        return response


def dashboard(request):
    naissances = Naissance.objects.all()
    deces = Deces.objects.all()
    nombre_naiss = naissances.count()
    nombre_deces = deces.count()
    context = {
        'naissances':naissances,
        'deces': deces,
        'nombre_naiss': nombre_naiss,
        'nombre_deces' : nombre_deces,
    
    }
    return render(request,'users/dashboard.html',context)

def loginPage(request):
   
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None :
            login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request, 'username or password is incorrect')
    context = {}
    return render(request, 'users/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    form = createNewUser()

    if request.method == 'POST':
        form = createNewUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {
        'form':form
    }
    return render(request, 'users/register.html', context)

def crudNaissance(request):
    naissances = Naissance.objects.all()
    context = {
        'naissances':naissances,
    }
    return render(request,'users/naissance.html',context)

def userPage(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request,'users/users.html',context)

class createProfile(CreateView):
    model = Utilisateur
    fields = ['telephone','statut','user']
    template_name = 'users/profile_utilisateur.html'
    success_url = reverse_lazy('dashboard')

def historique(request):
    hist = LogEntry.objects.all()
    context = {
        'hist': hist,
    }
    return render(request,'users/historique.html',context)

class CreateNaissance(CreateView):
    model = Naissance
    fields = '__all__'
    template_name = 'users/create_naissance.html'
    success_url = 'naissance'

class UpdateNaissance():
    pass