from django import forms
from assignmodformapp.models import project
class projectform(forms.ModelForm):
    class Meta:
        model = project
        fields = "__all__"