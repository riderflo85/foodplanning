from django import forms
from django.utils.functional import lazy
from .functions import list_key_save


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
        choices=lazy(list_key_save(_return_user_req()), tuple),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        ),
    )

    # A TESTER, PAS SUR !!!!
    def __init__(self, user):
        self.user_req = user

    def _return_user_req(self):
        return self.user_req