from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'room', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Ad', 
                'class': 'form-control'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Telefon', 
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email ünvanınız', 
                'class': 'form-control'
            }),
            'room': forms.Select(attrs={
                'class': 'form-control',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Mesaj yazın', 
                'class': 'form-control',
                'rows': 4
            }),
        }
        labels = {
            'name': 'Ad',
            'phone': 'Telefon',
            'email': 'Email Ünvanınız',
            'room': 'Otaq seçin',
            'message': 'Mesaj'
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        room_id = self.cleaned_data.get('room')
        if room_id:
            instance.room = room_id
        if commit:
            instance.save()
        return instance