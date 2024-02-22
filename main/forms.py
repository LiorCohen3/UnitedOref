from django import forms


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
        (1, 'Worm Food'),
        (2, 'Dry Food'),
        (3, 'Snacks'),
        (4, 'Winter Clothing'),
        (5, 'Summer Clothing'),
        (6, 'Underware'),
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
    auto_match = forms.BooleanField(required=False, label="Auto match")
