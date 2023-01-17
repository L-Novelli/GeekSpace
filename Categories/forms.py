from django import forms

class Games(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length= 10000)
    user = forms.CharField(max_length= 20)
    
    
class Cryptos(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length= 10000)
    user = forms.CharField(max_length= 20)

    

class Code(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length= 10000)
    user = forms.CharField(max_length= 20)
    

class Animes(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length= 10000)
    user = forms.CharField(max_length= 20)
   