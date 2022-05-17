from django.http import response
from django.shortcuts import render
from datetime import datetime

from .models import Services, Social_links, Timeline, Person, Company, Projects,Contact

# Create your views here.


def home(request):
    person = Person.objects.first()
    services = Services.objects.all()
    timeline = Timeline.objects.all()
    projects = Projects.objects.all()
    detail = Person.objects.get(pk=1)
    company = Company.objects.get(pk=1)
    links = Social_links.objects.get(pk=1)
    print(links.facebook)
    # print("------")
    # print(detail.phone)
    # print("------")
    # print("person ", person)
    context = {'person': person, 'services': services,
               'timeline': timeline, 'projects': projects, 'detail':detail, 'company': company}

    return render(request, 'index.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = Contact(name=name, email=email, date= datetime.today())
        contact.save()
        return render(request, 'contact.html')

    return render(request, 'contact.html')


# def project_section(request):
#     return render(request, 'project_section.html')


# def about_section(request):
#     return render(request, 'about_section.html')


# def contact_section(request):
#     return render(request, 'contact_section.html')


# def service_section(request):
#     return render(request, 'service_section.html')
