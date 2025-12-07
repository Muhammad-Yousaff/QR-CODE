from django import forms
class QRCodeForm(forms.Form):
    restaurant_name = forms.CharField(max_length=50, label='Restaurant Name')
    url=forms.URLField(max_length=200,label='Menu URL')