from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        # Inputlara stil vermek için (CSS sınıfları ekliyoruz)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınız Soyadınız'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-posta Adresiniz'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mesajınız...', 'rows': 5}),
        }