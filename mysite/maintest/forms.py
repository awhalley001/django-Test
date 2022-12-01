from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField()

class DocumentForm(forms.Form):
    file = forms.FileField(label='Select a file',help_text='max. 10 megabytes')

