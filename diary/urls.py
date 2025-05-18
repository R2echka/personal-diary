from django.urls import path

from . import views

app_name = "diary"

urlpatterns = [
    path("", views.Diary.as_view(), name="diary"),
    path("notes", views.Notes.as_view(), name="notes"),
    path("notes/<int:pk>", views.DetailedNote.as_view(), name="note"),
    path("notes/create", views.CreateNote.as_view(), name="new_note"),
    path("notes/<int:pk>/update", views.UpdateNote.as_view(), name="update_note"),
    path("notes/<int:pk>/delete", views.DeleteNote.as_view(), name="delete_note"),
]
