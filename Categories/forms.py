from django import forms

class Games(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length= 10000)
    
    
class Cryptos(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length= 10000)
    

class Code(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length= 10000)
    

class Animes(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length= 10000)
    