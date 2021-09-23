from django.shortcuts import render, redirect
from .models import Note, Tag   

def index(request): 
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        category = request.POST.get('categoria')
        category_note = Tag(name=category)
        if len(Tag.objects.filter(name=category)) > 0:
            new_note = category.note_set.create(title=title, content=content)
        else:
            category_note = Tag(name=category)
            new_note = Note(title=title, content=content, category=category_note)
            category_note.save() 
        new_note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all().order_by('id')
        return render(request, 'notes/index.html', {'notes': all_notes})

def edit_note(request, note_id):
    if request.method == 'POST':
        title = request.POST.get('edit_titulo')
        content = request.POST.get('edit_detalhes')
        category = request.POST.get('edit_categoria')
        note = Note.objects.get(pk=note_id)
        note.title = title
        note.content = content
        if len(Tag.objects.filter(name=category)) > 0:
            category = Tag(name=category)
            note.category = category
        else:
            new_category = Tag(name=category)
            new_category.save()
            note.category = new_category
        note.save()
        return redirect('index')
        
def delete_note(request, note_id):
    if request.method == 'POST':
        note = Note.objects.get(pk=note_id)
        if len(Tag.objects.filter(name=note.category.name)) > 1:
            pass
        else:
            tag = Tag.objects.get(name=note.category.name)
            tag.delete()
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