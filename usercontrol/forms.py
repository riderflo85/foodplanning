from django import forms


class LoginForm(forms.Form):
    """ Login form """

    user = forms.CharField(
        label='user',
        max_length=100,
        widget=forms.TextInput(
            attrs={'placeholder': 'Pseudo', 'class': 'form-control'}
            ),
    )
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Mot de passe', 'class': 'form-control'}
            ),
    )


class SignupForm(forms.Form):
    """ Register form """

    pseudo = forms.CharField(
        label='pseudo',
        max_length=30,
        widget=forms.TextInput(
            attrs={'placeholder': 'Pseudo', 'class': 'form-control'}
        ),
    )
    last_name = forms.CharField(
        label='nom',
        max_length=30,
        widget=forms.TextInput(
            attrs={'placeholder': 'Nom', 'class': 'form-control'}
        ),
    )
    first_name = forms.CharField(
        label='prénom',
        max_length=30,
        widget=forms.TextInput(
            attrs={'placeholder': 'Prénom', 'class': 'form-control'}
        ),
    )
    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(
            attrs={'placeholder': 'Email', 'class': 'form-control'}
        ),
    )
    password = forms.CharField(
        label='password',
        min_length=8,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Mot de passe', 'class': 'form-control'}
        ),
    )
    confirm_pwd = forms.CharField(
        label='confirm_pwd',
        min_length=8,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirmez votre mot de passe',
                'class': 'form-control'
            }
        ),
    )
    phone_number = forms.CharField(
        label='phone_number',
        max_length=9,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Numéro de portable pour être notifié',
                'class': 'form-control',
                'pattern': "[0-9]{1}[0-9]{2}[0-9]{2}[0-9]{2}[0-9]{2}"
            }
        ),
    )
    group_name = forms.CharField(
        label='group_name',
        max_length=45,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nom du foyer',
                'class': 'form-control'
            }
        ),
    )
