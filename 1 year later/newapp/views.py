from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView

# Create your views here.
# def Homepage(request):
#     return HttpResponse("hello user")
# def Contactpage(request):
#     return HttpResponse("u can contact us through our mail")
class HomePageView(TemplateView):
    template_name= 'Homepage.html'
class ContactPageView(TemplateView):
    template_name='contactpage.html'


