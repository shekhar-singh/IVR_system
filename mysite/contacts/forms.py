from django import forms
from django.core.validators import RegexValidator
from .models import Address, AudioFile
from django.forms import ModelForm, ModelChoiceField, Textarea, TextInput#, ModelMultipleChoiceField
from django.core.exceptions import ValidationError
 
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['id','name','email_id','address','phone_number']
        widgets = {
            'name': TextInput(attrs={'class':'form-control','name':'name','placeholder':'User Name'}),
            'email_id': TextInput(attrs={'class':'form-control form-control-solid placeholder-no-fix','placeholder':'Email'}),
            'address': TextInput(attrs={'class':'form-control form-control-solid placeholder-no-fix','placeholder':'Address'}),
            'phone_number': TextInput(attrs={'class':'form-control form-control-solid placeholder-no-fix','placeholder':'Phone number'}),
        
        }

    def clean_phone_number(self):
        phone_num=self.cleaned_data.get('phone_number', None)
        try:
            int(phone_num)
        except (ValueError, TypeError):
            raise ValidationError("Please enter a valid phone number")
        return phone_num


class AudioFileForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = ('speech', 'audio', )

# class TargetMembers(forms.Form):
#     members = forms.ModelMultipleChoiceField(queryset=Address.objects.all(), widget=forms.CheckboxSelectMultiple())


# class AddressPickerForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ('name', 'phone_number', )

#     def __init__(self, user, *args, **kwargs):
#         super(AddressPickerForm, self).__init__(*args, **kwargs)
#         self.queryset = Category.objects.all()


    
# class AddressPickerForm(forms.ModelForm):
#     Name = ModelMultipleChoiceField(queryset=Address.objects.all())
#     class Meta:      
#         model = Address
#         fields = ('name', 'phone_number',)