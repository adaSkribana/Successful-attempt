from django import forms


class ContactoForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=100)
    email = forms.EmailField(label="Email")
    message = forms.CharField(label="Descripcion", widget=forms.Textarea)
