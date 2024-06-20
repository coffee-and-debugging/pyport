from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from resume.models import contactform


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def projects(request):
    projects_showcase = [
        {
            "title": "Movie recommendation system",
            "path": "images/movie.png",
        },
        {
            "title": "Face Recognization",
            "path": "images/facerecon.png",
        },
        {
            "title": "Info Hunt",
            "path": "images/infohunt.png",
        },
        {
            "title": "3ntry Counter",
            "path": "images/entrycounter.png",
        },
        {
            "title": "Fake News Detection",
            "path": "images/fakenews.png",
        },
    ]
    return render(request, "projects.html", {"projects_showcase": projects_showcase})

def experience(request):
    experience = [
        {
            "company": "ZnepIT",
            "position": "CTO",
        },
        {
            "company": "Nexus Code n' Tech",
            "position": "Python Developer, Database Engineer",
        },
        {
            "company": "Fiverr",
            "position": "Data Expert",
        },
        {
            "company": "Upwork",
            "position": "Tech Consultant",
        },
    ]
    return render(request, "experience.html", {"experience": experience})

def certification(request):
    return render(request, "certification.html")

def contact(request):
    return render(request, "contact.html")

def resume(request):
    resume_path = "documents/resume.pdf"
    resume_path = staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path, "rb") as resume_file:
            response = HttpResponse(resume_file.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
            return response
    else:
        return HttpResponse("Resume not found", status=404)
    

def contactform(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        data=contactform(name=name, email=email, phone=phone, message=message)
        data.save()
    return render(request, "contact.html")
