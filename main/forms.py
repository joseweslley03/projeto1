from django import forms

class ContatoForm(forms.Form):
    assunto = forms.CharField(label="Assunto:",max_length=100)
    mensagem = forms.CharField(label="Mensagem:",widget=forms.Textarea)
    email = forms.EmailField(label="Email:")
    mecopiar = forms.BooleanField(label="Me copiar:")

