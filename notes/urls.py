from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_note/<note_id>', views.delete_note, name='delete-note'),
    path('edit_note/<note_id>', views.edit_note, name='edit-note'),
    path('category', views.show_category, name='show-category'),
    path('category/notes/<note_category>', views.categories, name='category-list'),
    path('category/notes/edit_note/<note_id>', views.edit_note, name='edit-note'),
    path('category/notes/delete_note/<note_id>', views.delete_note, name='delete-note')
]