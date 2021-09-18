from django import forms

# Cree sus formularios aquí:
class DatosUsers(forms.Form):
    identidy_user = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escoja un Usuario'}))
    telefono_user = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'60 XXX-XXX'}))
    describe_user = forms.CharField(label="", required=True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Profesional en el area de ...', 'rows':'5'}))
    linkedind_lnk = forms.URLField(label="", required=True, widget=forms.URLInput(attrs={'class':'form-control', 'placeholder':'http://LinkedIn/user'}))