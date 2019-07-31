from django import forms
from .list_all_dish import list_all_dish


class AddDishForms(forms.Form):
    name_dish = forms.CharField(
        label='name',
        max_length=160,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        ),
    )

class DelDishForms(forms.Form):
    del_dish = forms.ChoiceField(
        label='delete',
        choices=list_all_dish(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        ),
    )