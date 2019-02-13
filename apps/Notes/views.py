from django.shortcuts import HttpResponse, render, redirect

from .models import Note

def index(request):
    return render(request, "home.html")

def postnote(request):
    e = []
    if request.method == "POST":
        note = request.POST["note"]

        if len(note) < 1:
            e.append("Please type in a note")
            return HttpResponse(e, content_type = "application/json")
        elif len(note) < 10:
            e.append("Note must be at least 10 characters long")
            return HttpResponse(e, content_type = "application/json")
        else:
            Note.objects.create(note = note)
            return redirect("/notes")

def editnote(request, id):
    n = Note.objects.get(id = id)
    e = []
    
    if request.method == "POST":
        note = request.POST["note"]

        if len(note) < 1:
            e.append("Please type in a note")
            return HttpResponse(e, content_type = "application/json")
        elif len(note) < 10:
            e.append("Must be at least 10 characters long")
            return HttpResponse(e, content_type = "application/json")
        else:
            n.note = note
            n.save()
            return redirect("/notes")

def deletenote(request, id):
    Note.objects.get(id = id).delete()
    return redirect("/notes")

def allnotes(request):
    return render(request, "notes.html", {"notes": Note.objects.all()} )