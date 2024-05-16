from django.shortcuts import render
from django.views import View
from django.contrib import messages
from . import static_data

# Create your views here.
context = {'menu_items': static_data.dashboard_menu_items}

class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard/dashboard.html', context)

class AddBlogsView(View):
    def get(self, request):
        return render(request, 'dashboard/dashboard.html', context)
