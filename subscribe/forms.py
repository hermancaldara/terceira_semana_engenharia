from django import forms
from models import Subscribe

class SubscribeForm(forms.ModelForm):
    
    class Meta:
        model = Subscribe
        exclude = ('first_short_course','second_short_course',)