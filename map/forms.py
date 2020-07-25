#can delete this file

from django import forms

#TO DO: extract this list from excel
COUNTRY_CHOICES = [
    ('Afghanistan', 'Afghanistan'),
    ('Albania', 'Albania'),
]

class CountriesForm(forms.Form):
    country = forms.CharField(label='Which country would you like to explore?',
        widget=forms.Select(choices=COUNTRY_CHOICES))
