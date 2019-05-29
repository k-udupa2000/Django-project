from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    model = User
    username = forms.CharField(max_length = 100,)
    password = forms.CharField(widget = forms.PasswordInput,)

'''
class RegistrationForm(forms.Form):
    email = forms.EmailField(required = True)
    phone_regex = RegexValidator(regex = r'^[0-9]{10}$', message = "Phone number must be of the form: 9876543210.")
    phonenumber1 = models.CharField(validators = [phone1_regex], max_length = 11)
    phonenumber2 = models.CharField(validators = [phone1_regex], max_length = 11, blank = True)

    class Meta:
        model = User
        fields = (
            'username',, verbose_name = "Secondary Phone No.",
            'email',
            'password1',
            'phonenumber1',
            'phonenumber2'
        )

        def save(self, commit = True):
            user = super(RegistrationForm, self.save(commit = False))
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']

            if commit:
                user.save()
            return user
'''