from django.shortcuts import render,HttpResponse
from datetime import datetime
from .models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "variable":"this is my variable"
    }
    
    return render(request,'index.html',context)
  #  return HttpResponse("this is Home page")

def About(request):
    return render(request,'about.html')

   # return HttpResponse("this is About page")

def Profile(request):
    return render(request,'Profile.html')
  #  return HttpResponse("this is profile page")

def Services(request):
    return render(request,'services.html')
  #  return HttpResponse("this is Services page")

def contact_view(request):
    if request.method == 'POST':
     name=request.POST.get('name')
     email=request.POST.get('email')
     phone=request.POST.get('phone')
     address=request.POST.get('address')
     message = request.POST.get('message')
     date=request.POST.get('date')
     new_contact =Contact(name=name,email=email,phone=phone,address=address,message=message,date=datetime.today())
     new_contact.save()
     messages.success(request,'Your message has been sent!')
    return render(request,'contact.html')

  #  return HttpResponse("this is Contact page")

    
def terms(request):
    return render(request, 'terms.html')

def track_order(request):
    return render(request, 'track_order.html') 

def returns_refunds(request):
    return render(request, 'returns_refunds.html') 

def newsletter_subscribe(request):
    return render(request, 'news.html') 



def faqs(request):
    return render(request, 'faqs.html') 

def my_account(request):
    return render(request, 'my_account.html') 

def investor_relation(request):
    return render(request, 'investor_relation.html') 

def careers(request):
    return render(request, 'careers.html') 

def gift_vouchers(request):
    return render(request, 'gift_vouchers.html') 

def community_initiatives(request):
    return render(request, 'community_initiatives.html') 



def terms_conditions(request):
    return render(request, 'terms_conditions.html') 

def privacy_policy(request):
    return render(request, 'privacy_policy.html') 

def sitemap(request):
    return render(request, 'sitemap.html') 

def blogs(request):
    return render(request, 'blogs.html') 