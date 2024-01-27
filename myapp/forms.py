from django import forms
from.models import Member1


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member1
        fields = ['firstname','lastname','rollno']

   
        