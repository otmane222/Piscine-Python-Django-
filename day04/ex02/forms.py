from django import forms

class Text(forms.Form):
    text_input = forms.CharField(label='Enter Text', max_length=50)

    




#     class RegistrationForm(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)