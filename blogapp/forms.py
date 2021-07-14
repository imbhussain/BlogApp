from django import forms
from .models import Post

# Created model form for Post Model

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','body','img']

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),  
        }
