from django import forms
from django.core import validators



def check_for_a(value):
    if value[0]=='d':
        raise forms.ValidationError('name start with s')

class StudentForm(forms.Form):
    Sname=forms.CharField(max_length=100,validators=[check_for_a])
    Sage=forms.IntegerField()
    Sid=forms.IntegerField()
    Semail=forms.EmailField()
    Remail=forms.EmailField()
    mobile=forms.CharField(min_length=10,max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])

    def clean(self):
        sm=self.cleaned_data['Semail']
        rm=self.cleaned_data['Remail']
        if sm != rm:
            raise forms.ValidationError('mails not matched')