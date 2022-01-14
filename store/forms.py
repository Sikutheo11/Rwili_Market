from django import forms
from .models import ReviewRating
from .models import Product

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']


# create a ModelForm
class ProductForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Product
        fields = "__all__"
