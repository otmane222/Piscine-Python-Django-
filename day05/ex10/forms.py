from django import forms
from .models import People



class Search(forms.Form):
    minimum_date = forms.DateField(
        label='Movies minimum release date',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    maximum_date = forms.DateField(
        label='Movies maximum release date',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    diameter_num = forms.IntegerField(label='Planet diameter greater than')
    GENDER_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # Fetch unique gender values from People model and populate dropdown
    #     gender_choices = People.objects.values_list('gender', 'gender').distinct()
    #     self.fields['character_gender'] = forms.ChoiceField(
    #         choices=gender_choices,
    #         label='Character gender',
    #         widget=forms.Select(attrs={'class': 'form-control'})
    #     )