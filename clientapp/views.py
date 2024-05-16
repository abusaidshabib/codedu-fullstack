from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login

# Created files
from .forms import RegistrationForm, LoginForm
from . import static_data

# Create your views here.
context = {'menu_items': static_data.menu_items,'courses':static_data.courses, 'blogs': static_data.blogs}

class HomeView(View):
    def get(self, request):
        return render(request, 'clientapp/home.html', context)

class CategoriesView(View):
    def get(self, request):
        return render(request, 'clientapp/categories.html', context)

class AboutView(View):
    def get(self, request):
        return render(request, 'clientapp/about.html', context)

class BlogView(View):
    def get(self, request):
        return render(request, 'clientapp/blog.html', context)

class FaqView(View):
    def get(self, request):
        return render(request, 'clientapp/faq.html', context)

class LoginView(View):
    template_name = 'common/login.html'

    def get(self, request):
        form = LoginForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect('main_home')
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Invalid email or password.")

        context = {'form': form}
        return render(request, self.template_name, context)

class RegisterView(View):
    template_name = 'common/register.html'

    def get(self, request):
        form = RegistrationForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations!! You have become an Author.')
            return redirect(reverse_lazy('main_home'))  # Adjust this to the appropriate URL name
        else:
            context = {'form': form}
            return render(request, self.template_name, context)