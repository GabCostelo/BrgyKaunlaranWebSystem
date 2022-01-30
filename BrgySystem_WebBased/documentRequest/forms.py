from django import forms
from accounts.models import User
from documentRequest.models  import docType,BrgyIndigency,BrgyClearance,BrgyResidency


#BrgyIndigency
class brgyIndigencyForm(forms.ModelForm):
    first_name = forms.CharField(required=True,label='First Name')
    last_name = forms.CharField(required=True,label='Last Name')
    middle_name = forms.CharField(required=False,label='Middle Name')
    age = forms.CharField(required=True)
    nationality = forms.CharField(required=True)
    purpose = forms.CharField(required=True)
    email = forms.EmailField()
    cedula = forms.ImageField(required=False)
    validId = forms.ImageField(required=False,label='Valid ID')
    otherDocument = forms.ImageField(required=False,label='Other Documents')
    is_Pending = True

    class Meta:
        model=BrgyIndigency
        fields = ['first_name','last_name','middle_name','age','nationality',
                'purpose','Address','email','cedula','validId','otherDocument','requested_by']
        widgets = {
            'requested_by': forms.TextInput(attrs={'class':'form','value':'','id':'elder','type':'hidden'}),
        }

#BrgyClearance
class brgyClearanceForm(forms.ModelForm):
    first_name = forms.CharField(required=True,label='First Name')
    last_name = forms.CharField(required=True,label='Last Name')
    middle_name = forms.CharField(required=False,label='Middle Name')
    age = forms.CharField(required=True)
    nationality = forms.CharField(required=True)
    purpose = forms.CharField(required=True)
    email = forms.EmailField()
    cedula = forms.ImageField()
    is_Pending = True
    class Meta:
        model=BrgyClearance
        fields = ['first_name','last_name','middle_name','age','nationality',
                'purpose','Address','email','cedula','requested_by']
        widgets = {
            'requested_by': forms.TextInput(attrs={'class':'form','value':'','id':'elder','type':'hidden'}),
        }


#BrgyResidency
class brgyResidencyForm(forms.ModelForm):
    first_name = forms.CharField(required=True,label='First Name')
    last_name = forms.CharField(required=True,label='Last Name')
    middle_name = forms.CharField(required=False,label='Middle Name')
    age = forms.CharField(required=True)
    nationality = forms.CharField(required=True)
    purpose = forms.CharField(required=True)
    email = forms.EmailField()
    cedula = forms.ImageField()
    validId = forms.ImageField(label='Valid ID')
    is_Pending = True

    class Meta:
        model=BrgyResidency
        fields = ['first_name','last_name','middle_name','age','nationality',
                'purpose','Address','email','cedula','validId','requested_by']
        widgets = {
            'requested_by': forms.TextInput(attrs={'class':'form','value':'','id':'elder','type':'hidden'}),
        }
