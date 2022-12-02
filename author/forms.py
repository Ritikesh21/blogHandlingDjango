from django import forms

from .models import *


class RegistrationForm(forms.ModelForm):
	# firstName = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'First Name'}))
    # lastName = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Last Name'}))
    # email = forms.CharField(widget= forms.EmailInput(attrs={'placeholder':'First Name'}))

	class Meta:
		model = Author
		fields = '__all__'