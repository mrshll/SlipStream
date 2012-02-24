from django import forms

class AddShowForm(forms.Form):
    show_name = forms.CharField(max_length=100)