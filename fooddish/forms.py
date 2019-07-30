from django import forms


class AddDishForms(forms.Form):
    name_dish = forms.CharField(
        label='name',
        max_length=160,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        ),
    )