from django.shortcuts import render, redirect
from .models import Note, Tag   

def index(request): 
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        category = request.POST.get('categoria')
        new_category = Tag(name=category)
        new_category.save()
        new_note = Note(title=title, content=content, category=new_category)
        new_note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def edit_note(request, note_id):
    if request.method == 'POST':
        title = request.POST.get('edit_titulo')
        content = request.POST.get('edit_detalhes')
        note = Note.objects.get(pk=note_id)
        note.title = title
        note.content = content
        note.save()
        return redirect('index')
        
def delete_note(request, note_id):
    if request.method == 'POST':
        note = Note.objects.get(pk=note_id)
        note.delete()
        return redirect('index')

def show_category(request):
    all_notes = Note.objects.all()
    return render(request, 'notes/category.html', {'notes': all_notes})

def categories(request, note_category):
    tag = Tag.objects.get(name=note_category)
    print(tag)
    all_notes = Note.objects.filter(category=tag)
    return render(request, 'notes/notes.html', {'notes': all_notes})