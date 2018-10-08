from django.shortcuts import render
from django.urls import reverse_lazy
# Those are import to use class based view
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from . import models
# from django.http import HttpResponse
# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    # Normally return as school_list
    # In terms of personal develp, school_list is okay
    # But when makeing big program with the group, better use "context_object_name"

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
# The function below for the function based view


# This is class based view
# class CBView(View):
#     def get(self,request):
#         return HttpResponse("Class based View are COOL")


#
# # **jwargs will give you all keywird arguments and treat as a dictionaly
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = 'Basic injection'
#         return context
