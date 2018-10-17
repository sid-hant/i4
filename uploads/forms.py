from django import forms
from .models import Upload
 
class Submit(forms.ModelForm):
    
    
    class Meta():
        model = Upload
        fields = ['message','file1','file2','file3','file4','file5'] 
        labels = {'message':  'Message', 'file1': "", 'file2': "", 'file3': "", 'file4': "", 'file5': ""}
        widgets = {
            'file1' : forms.FileInput(attrs={'class': 'btn btn-outline-dark btn-lg btn-block'}),
            'file2' : forms.FileInput(attrs={'class': 'btn btn-outline-dark btn-lg btn-block'}),
            'file3' : forms.FileInput(attrs={'class': 'btn btn-outline-dark btn-lg btn-block'}),
            'file4' : forms.FileInput(attrs={'class': 'btn btn-outline-dark btn-lg btn-block'}),
            'file5' : forms.FileInput(attrs={'class': 'btn btn-outline-dark btn-lg btn-block'})
        } 

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)