from django import forms
from django.contrib.auth.models import User
from books.models import Book
 
# using my_date_formats = ['%d/%m/%Y',] we can ocerride the default input format provided by django

MY_DATE_FORMATS = ['%d/%m/%Y',]


class bookForm(forms.ModelForm):
    publicatin_date = forms.DateField(input_formats=MY_DATE_FORMATS)

    class Meta:
        model = Book
        fields = ('title','descrp', 'authors', 'publisher', 'publicatin_date',)
        

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Email Address')
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words ")
        return message


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
