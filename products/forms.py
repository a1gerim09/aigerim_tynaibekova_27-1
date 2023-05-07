from django import forms


class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False)
    name = forms.CharField(min_length=2, max_length=254)
    description = forms.CharField(widget=forms.Textarea())
    price = forms.FloatField()


class ReviewCreateForm(forms.Form):
    text = forms.CharField(min_length=2, max_length=254)