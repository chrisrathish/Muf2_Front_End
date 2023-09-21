from django import forms

class DocumentForm(forms.Form):
    document = forms.FileField(label='Select a file')