from django import forms

class VerifyForm(forms.Form):
    verify_membership_file = forms.FileField(label='Please upload an image', )