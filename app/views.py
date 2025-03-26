from django.http import HttpRequest
from django.shortcuts import render, HttpResponse
from app.models import NoteInfo

# Create your views here.

def index(request):
    return HttpResponse("主页")

def note_page(request: HttpRequest, id):
    if len(id) > 64:
        return HttpResponse("ID长度超出限制")
    content = ""
    try:
        content = NoteInfo.objects.get(note_id = id).content
    except NoteInfo.DoesNotExist:
        ...
    return render(request, "note_page.html", {"id": id, "content": content})

def update(request: HttpRequest, id):
    if len(id) > 64:
        return HttpResponse("ID长度超出限制")
    if request.method == "POST":
        content = request.POST.get("content")
        try:
            NoteInfo.objects.get(note_id = id)
        except NoteInfo.DoesNotExist:
            note = NoteInfo(note_id = id, content = "")
            note.save()
            
        note = NoteInfo.objects.get(note_id = id)
        note.content = content
        note.save()
        print(NoteInfo.objects.get(note_id = id).content)
        
        return HttpResponse("OK")
    else:
        return HttpResponse("Error")
    
def backend_list(request: HttpRequest):
    notes = NoteInfo.objects.all()
    list = []
    for note in notes:
        if len(note.content) != 0:
            list.append({
                "id": note.note_id,
                "length": len(note.content)
            })
    list = sorted(list, key=lambda x: x["id"])
    return render(request, "backend_list.html", {"list": list})