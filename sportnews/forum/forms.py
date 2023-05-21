from django import forms
from .models import Comments, Treads
import re
from django.core.exceptions import ValidationError



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment_text']
        widgets = {
            'comment_text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
            }),
        }

class TreadsForm(forms.ModelForm):
    class Meta:
        model = Treads
        # fields = '__all__'
        fields = ['title', 'discription']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'discription': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
            }),
        }
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title