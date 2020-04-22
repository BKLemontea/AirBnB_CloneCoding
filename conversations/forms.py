from django import forms

class AddComementForm(forms.Form):
    
    message = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': "Add a Comment"}))