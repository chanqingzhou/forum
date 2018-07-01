from django import forms
from .models import AnswerFile, Comments

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = AnswerFile
        fields =['title','file']



class Commentform(forms.ModelForm):
    class Meta:
        model= Comments
        fields =['user','text']