from django import forms
from app.models import * 
class Topic_modelform(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'
        
class Webpage_modelform(forms.ModelForm):
    class Meta:
        model = Webpage
        fields = '__all__'

class Access_modelform(forms.ModelForm):
    class Meta:
        model = Access_records
        fields = '__all__'