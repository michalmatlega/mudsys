__author__ = 'Krzysiek'

from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Wybierz plik',
        help_text='maks. 1GB'
    )
