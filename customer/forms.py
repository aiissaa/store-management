from django import forms
from django.contrib.auth import get_user_model
from customer.models import Customer

class SignUpForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            # add form-control class to all fields
            self.fields[field].widget.attrs['class'] = 'form-control'
            # add placeholder to all fields
            self.fields[field].widget.attrs['placeholder'] = self.fields[field].label        
            # add text-white class all labels
            self.fields[field].label_attrs = {'class': 'text-white'}

    class Meta:
        model = get_user_model()
        fields = ('username', 'email')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        if commit:
            user.save()
        return user


class CustomerAdminForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude =  ('created_by', )
