import re

from django import forms

from order.models import Order


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['city', 'address', 'address_optional', 'postal_code']
        widgets = {
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Moscow'
            }),
            'address': forms.TextInput(attrs={
                'placeholder': 'Stroiteley d.3'
            })
        }

    def clean_address(self):
        address = self.cleaned_data['address']
        if not re.search(r'\d', address):
            self.add_error('address', 'Address must have at least 1 digit')
        return address

    def clean_postal_code(self):
        postal_code = self.cleaned_data['postal_code']
        if not re.match(r'^[1-9]\d{5}$', postal_code):
            self.add_error('postal_code', 'Please provide a valid postal code')
        return postal_code
