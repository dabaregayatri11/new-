from django.contrib import admin
from django.urls import path
from home import views
from .views import contact_view

urlpatterns = [
   path("", views.index,name='Home'),
   path("About", views.About,name='About'),
   path("Profile", views.Profile,name='Profile'),
   path("Services", views.Services,name='Services'),
   #path("Contact", views.Contact,name='Contact'),
   path('terms', views.terms, name='Terms'),
   path('track-order/', views.track_order, name='track_order'),
   path('returns/', views.returns_refunds, name='returns_refunds'),
    # ... add all other URL patterns
   path('news/', views.newsletter_subscribe, name='newsletter_subscribe'),
   path('faqs/', views.faqs, name='faqs'),

   path('my_account/', views.my_account, name='my_account'),
   
     path('investor_relation/', views.investor_relation, name='investor_relation'),
      path('careers/', views.careers, name='careers'),
       path('gift_vouchers/', views.gift_vouchers, name='gift_vouchers'),
        path('community_initiatives/', views.community_initiatives, name='community_initiatives'),
         path('terms_conditions/', views.terms_conditions, name='terms_conditions'),
          path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
           path('sitemap/', views.sitemap, name='sitemap'),
            path('blogs/', views.blogs, name='blogs'),
            path('Contact', contact_view, name='Contact'),

]
