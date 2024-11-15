from django import forms
from .models import postModel,  comment

class postModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))
    class Meta:
        model = postModel
        fields = ('title', 'content', )

class commentForm(forms.ModelForm):

    class Meta:
        model = comment
        fields = ('content', )