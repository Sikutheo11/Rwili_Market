from django import forms
from .models import Order, Address
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'email', 'country', 'province', 'district', 'sector', 'cell', 'village', 'order_note']



class AddressForm(forms.Form):
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.CharField()
	phone = forms.CharField()
	country = CountryField(blank_label="Select country").formfield(widget=CountrySelectWidget(attrs={"class": "custom-select d-block w-100"
	}))
	province = forms.CharField()
	district= forms.CharField()
	sector= forms.CharField()
	cell = forms.CharField()
	village = forms.CharField()
	nearest_market = forms.CharField()
	nearest_Agakiriro = forms.CharField()
	save_info = forms.BooleanField(required=False)
	use_default = forms.BooleanField(required=False)
	
