from django.urls import path
# from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('about', views.about, name="about"),
    # path('service', views.service, name="service"),
    # path('timeline', views.timeline, name="timeline"),
    # path('projects', views.projects, name="projects"),
    path('contact', views.contact, name="contact"),
    # path('project_section', views.project_section, name="project_section"),
    #  path('about_section', views.about_section, name="about_section"),
    #   path('contact_section', views.contact_section, name="contact_section"),
    #    path('service_section', views.service_section, name="service_section"),

]
