from django import forms
from contact_app.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['subject', 'email', 'text']
        widgets = {
        'subject': forms.TextInput(attrs={
            'id':'content-subject',
            'placeholder':'Subject',
            'required': True
            }),
        'email': forms.EmailInput(attrs={
            'id':'contact-email',
            'placeholder':'Email',
            'required': True
            }),
        'text': forms.Textarea(attrs={
            'id':'contact-text',
            'placeholder':'Text',
            'required': True
            }),

        }