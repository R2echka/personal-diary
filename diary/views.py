from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, View)

from diary.forms import NoteForm
from diary.models import Note


# Create your views here.
class Diary(View):
    model = Note
    template_name = "diary/diary.html"

    def get(self, request):
        return render(request, "diary/diary.html")


class Notes(LoginRequiredMixin, ListView):
    model = Note
    template_name = "diary/notes.html"
    context_object_name = "notes"

    def get_queryset(self):
        text = self.request.GET.get("search", None)
        if text:
            return Note.objects.filter(
                Q(owner=self.request.user)
                & (Q(title__icontains=text) | Q(note__icontains=text))
            )
        return Note.objects.filter(owner=self.request.user)


class DetailedNote(LoginRequiredMixin, DetailView):
    model = Note
    template_name = "diary/note.html"
    context_object_name = "note"


class CreateNote(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = "diary/note_form.html"
    success_url = reverse_lazy("diary:notes")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class UpdateNote(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "diary/note_form.html"
    success_url = reverse_lazy("diary:notes")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return self.form_class
        raise PermissionDenied


class DeleteNote(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = "diary/delete_note.html"
    success_url = reverse_lazy("diary:notes")

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
