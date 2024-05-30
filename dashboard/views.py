from django.shortcuts import render
from django.views import View
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from . import static_data

from .forms import CoursesForm

# Create your views here.
context = {'menu_items': static_data.dashboard_menu_items}

class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard/dashboard.html', context)


class AddBlogsView(View):
    def get(self, request):
        return render(request, 'dashboard/dashboard.html', context)

class AddCoursesView(FormView):
    template_name = 'dashboard/addcourses.html'
    form_class = CoursesForm
    success_url = reverse_lazy('successful')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data here
        context['menu_items'] = static_data.dashboard_menu_items
        return context

    def form_valid(self, form):
        print(form.cleaned_data)
        form.save()
        print("data saved successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"Error in {field}: {error}")
        return super().form_invalid(form)

class SuccessfulView(View):
    def get(self, request):
        return render(request, 'common/successful.html', context)