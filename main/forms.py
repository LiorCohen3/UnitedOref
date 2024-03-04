from django import forms
from django.db import models
from .models import item_type


class DonationForm(forms.Form):
    AREA_CHOICES = [
        ('North', 'North'),
        ('Center', 'Center'),
        ('South', 'South'),
    ]
    DONATION_TYPE = [
        (1, 'Food'),
        (2, 'Equipment')
    ]

    ITEM_TYPE_CHOICES = [
        (1, 'Warm Food'),
        (2, 'Dry Food'),
        (3, 'Snacks'),
        (4, 'Winter Clothing'),
        (5, 'Summer Clothing'),
        (6, 'Underwear'),
        (7, 'Socks'),
        (8, 'Tactical Vests'),
        (9, 'Tactical Gloves'),
        (10, 'Tactical Uniform'),
        (11, 'Tactical Boots'),
        (12, 'Tactical Protection'),
        (13, 'Tactical Helmets'),
    ]

    area = forms.ChoiceField(choices=AREA_CHOICES)
    item_type = forms.ChoiceField(choices=ITEM_TYPE_CHOICES)
    donation_type = forms.ChoiceField(choices=DONATION_TYPE)
    count = forms.IntegerField()


class EditProfileForm(forms.Form):
    first_name = forms.CharField(max_length=45, required=True)
    last_name = forms.CharField(max_length=45, required=True)
    phone = forms.CharField(max_length=45, required=True)
    email = forms.EmailField(max_length=254, required=True)


class NewRequest(forms.Form):
    AREA_CHOICES = [
        ('North', 'North'),
        ('Center', 'Center'),
        ('South', 'South'),
    ]

    all_objects = item_type.objects.values('description')
    item_name = forms.ChoiceField(choices=[(obj['description'], obj['description']) for obj in all_objects])

    area = forms.ChoiceField(choices=AREA_CHOICES)
    info = forms.CharField(max_length=45, required=True)
    item_quantity = forms.IntegerField(required=True)
    requestor = forms.IntegerField(required=True)
    item_type = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Exclude 'requestor' field from the form
        if 'requestor' in self.fields:
            del self.fields['requestor']
            del self.fields['item_type']


class LocationForm(forms.Form):
    location_lat = forms.CharField(widget=forms.HiddenInput)
    location_long = forms.CharField(widget=forms.HiddenInput)
