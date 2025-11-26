from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.views import View
from viewer.models import Item
from django.views.generic import TemplateView, ListView, FormView
from viewer.forms import ItemForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test

def hello(request, s): 
    return HttpResponse(f'Hello, prieten atv-ist {s}!')

def home_page(request):
    return render(request, "home.html")

def items_list(request, type_id):
    atv_list = Item.objects.filter(Type=type_id)
    print(atv_list)  # să vedem în terminal dacă există obiecte
    return render(request, "itemslist.html", {'atv_list': atv_list})


# class ItemView(View):
#     def get(self, request, type_id):
#         return render(
#             request,
#             template_name='item.html',
#             context={'item': Item.objects.filter(Type=type_id)}
#         )
    
class ItemCreateView(FormView):
    template_name = 'viewer/form.html'
    form_class = ItemForm

def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def get_success_url(self):
        return '/'

class ItemCreateView2(FormView):
    template_name = 'form.html'
    form_class = ItemForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return '/'


def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def add_item(request):
    if request.method == 'POST':
        type_id = request.POST.get("Type")
        matched_type = get_object_or_404(Type, pk=type_id)
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('a mers')
            return redirect('items_list', type_id=matched_type.id)
        else:
            print('Nu a mers!', form.errors)
    else:
        form = ItemForm()
        print('Nu a mers!')
    return render(request, 'add_item.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Contul tau a fost creat cu succes, acum te poti loga !")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bun venit inapoi, {username}!")
                return redirect('home')  # sau unde vrei să redirecționezi după login
        messages.error(request, "Nume de utilizator sau parola incorecte! .")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, "Te-ai deconectat cu succes!.")
    return redirect('home')

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, "Felicitări! Te-ai logat cu succes! 🚀")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')
    
def my_account(request):
    return render(request, 'my_account.html')