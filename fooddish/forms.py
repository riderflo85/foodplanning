from django import forms
from django.utils.functional import lazy
from .list_all_dish import list_all_dish


class AddDishForms(forms.Form):
    """ Form used for user add new dish in the database """

    name_dish = forms.CharField(
        label='name',
        max_length=160,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        ),
    )


class DelDishForms(forms.Form):
    """ Form used for user to delete a dish in the database """

    del_dish = forms.ChoiceField(
        label='delete',
        choices=lazy(list_all_dish, tuple),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        ),
    )
