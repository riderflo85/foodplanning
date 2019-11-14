from django import forms
from django.utils.functional import lazy
from .functions import all_key_save


class SeeAnotherPlanningForm(forms.Form):
    user = None
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
        choices=all_key_save(user),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        ),
    )

    def __init__(self, req_user):
        user = req_user