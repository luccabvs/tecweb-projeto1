from django.shortcuts import render, redirect
from .models import Note, Tag   

def index(request): 
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        category = request.POST.get('categoria').upper()
        if len(Tag.objects.filter(name=category)) > 0:
            new_note = Note(title=title, content=content, category=Tag.objects.get(name=category))
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
        category = request.POST.get('edit_categoria').upper()
        note = Note.objects.get(pk=note_id)
        note.title = title
        note.content = content
        old_category = note.category
        if len(Note.objects.filter(category=old_category)) <= 1:
            tag = Tag.objects.get(name=note.category.name)
            tag.delete()
        if len(Tag.objects.filter(name=category)) > 0:
            note.category = Tag.objects.get(name=category)
        else:
            print('tchau')
            new_category = Tag(name=category)
            new_category.save()
            note.category = new_category
        note.save()
        return redirect('index')
        
def delete_note(request, note_id):
    if request.method == 'POST':
        note = Note.objects.get(pk=note_id)
        category = note.category
        if len(Note.objects.filter(category=category)) > 1:
            pass
        else:
            tag = Tag.objects.get(name=note.category.name)
            tag.delete()
        note.delete()
        return redirect('index')

def show_category(request):
    if request.method == 'GET':
        all_categories = Tag.objects.exclude(name='')
        return render(request, 'notes/category.html', {'categories':all_categories})

def categories(request, note_category):
    tag = Tag.objects.get(name=note_category)
    all_notes = Note.objects.filter(category=tag)
    return render(request, 'notes/notes.html', {'notes': all_notes})