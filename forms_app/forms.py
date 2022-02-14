from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='E-Mail')
    category = forms.ChoiceField(
        choices=[('question', 'Question'), ('other', 'Other'), ('age', 'AGE')])
    body = forms.CharField()
