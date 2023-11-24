from django import forms

class ComicForm(forms.Form):
    text = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Enter the Name'}))