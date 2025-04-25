from django import forms

from diary.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "note"]

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Заголовок"}
        )
        self.fields["note"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Начните писать"}
        )
