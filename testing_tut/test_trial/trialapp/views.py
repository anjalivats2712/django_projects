from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Homepage(TemplateView):
    template_name="index.htm"
class Aboutpage(TemplateView):
    template_name="about.htm"

