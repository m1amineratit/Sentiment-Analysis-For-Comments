from django import forms

class CommentForm(forms.Form):
    text = forms.CharField(
        label="Enter ur comments",
        widget=forms.Textarea(attrs={'rows' : 3, 'class' : 'form-control'})
    )