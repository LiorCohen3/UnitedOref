from django import forms
from django.contrib.auth.forms import UserCreationForm
from main.models import CustomUser


class CustomUserForm(UserCreationForm):
    phone = forms.CharField(max_length=45, required=True)
    real_id = forms.CharField(max_length=9, required=True)
    # unit = forms.CharField(max_length=45, required=True)
    first_name = forms.CharField(max_length=45, required=True)
    last_name = forms.CharField(max_length=45, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'phone', 'real_id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
        self.fields['password2'].help_text = None

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def valid_real_id(self):
        sum = 0
        for index, val in enumerate(self.real_id):
            val = int(val)
            if index == 8:
                if val == 10 - (sum % 10):
                    return True
                else:
                    return False
            elif index % 2 == 0:
                sum += val
            else:
                if val * 2 > 9:
                    sum += val * 2 % 10
                    sum += val * 2 // 10
                else:
                    sum += (val * 2)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
