from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.form_method = 'post'
        self.helper.add_input(CustomButton('submit', 'Submit'))


class CustomButton(Button):
    # removed default btn class and added custom
    def __init__(self, *args, **kwargs):
        self.field_classes = 'btn-custom-form'
        self.input_type = 'submit'
        super(Button, self).__init__(*args, **kwargs)
