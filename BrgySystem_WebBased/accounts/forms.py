from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from accounts.models import User,Constituent

class ConstituentCreateForm(UserCreationForm):

    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True,label='First Name')
    middle_name = forms.CharField(required=False,label='Middle Name')
    last_name = forms.CharField(required=True,label='Last Name')
    Address = forms.CharField(required=True,label='Address')

    class Meta(UserCreationForm.Meta):
        model = User
        fields =['email','first_name','middle_name','last_name','username','Address']
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('first_name')
        user.middle_name = self.cleaned_data.get('middle_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.Address = self.cleaned_data.get('Address')
        user.is_Constituent = True
        user.is_active = False
        user.save()
        constituent = Constituent.objects.create(user=user)
        constituent.email = self.cleaned_data.get('email')
        constituent.first_name = self.cleaned_data.get('first_name')
        constituent.middle_name = self.cleaned_data.get('middle_name')
        constituent.last_name = self.cleaned_data.get('last_name')
        constituent.Address = self.cleaned_data.get('Address')
        constituent.save()
        return user
