from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexr,name='indexr'),
    path('ATS', views.ATS, name='ATS'),
    path('Communication', views.Communication,name='Communication'),
    path('interView_candidate/<int:job_id>/<int:applicant_id>/', views.interView_candidate, name='interView_candidate'),
    path('shortlist_candidate/<int:job_id>/<int:applicant_id>/', views.shortlist_candidate, name='shortlist_candidate'),
    path('Review_candidate/<int:job_id>/<int:applicant_id>/', views.Review_candidate, name='Review_candidate'),
    path('mail_candidate/<int:job_id>/<int:applicant_id>/', views.mail_candidate, name='mail_candidate'),
    path('downloadresume_candidate/<int:job_id>/<int:applicant_id>/', views.downloadresume_candidate, name='downloadresume_candidate'),
    path('Interview', views.Interview,name='Interview'),
    path('Jobposting', views.Jobposting,name='Jobposting'),
    path('Shortlisted', views.Shortlisted,name='Shortlisted'),
    path('sample', views.sample,name='sample'),
   ]