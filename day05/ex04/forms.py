from django import forms

class Formo(forms.Form):
    title = forms.TextInput(label='Enter Title', max_length=100)