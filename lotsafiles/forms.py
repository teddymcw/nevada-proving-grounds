from django import forms

class VerifyForm(forms.Form):
    verify_membership_file = forms.FileField(label='Please upload an image', )



class AgainVerifyForm(forms.Form):
    again_ver_file = forms.FileField(label='Again, please upload an image', )