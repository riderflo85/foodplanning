import functools 
from django import forms
from django.utils.functional import lazy
from .functions import all_key_save


def all_key_partial(user):
    return lazy(functools.partial(all_key_save, user), tuple)


class SeeAnotherPlanningForm(forms.Form):
    secret_key = forms.CharField(
        label='secret_key',
        widget=forms.TextInput(
            attrs={
                'placeholder': "Clé secrète de l'utilisateur",
                'class': 'form-control'
            },
        )
    )

    key_save = forms.ChoiceField(
        label='key_save',
        choices=all_key_partial(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        ),
    )
