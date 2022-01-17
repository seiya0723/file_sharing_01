from django import forms

from .models import Document

class DocumentForm(forms.ModelForm):

    class Meta:
        model   = Document
        #mimeを追加する。userも追加する。
        fields = ["name", "content", "mime", "user"]
