from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _

from .models import User

class RegistrationForm(UserCreationForm):
    """
    User Registration form for register new users
    """
    # password1 = ReadOnlyPasswordHashField(
    #     label=_("Password"),
    #     help_text=_(
    #         "Raw passwords are not stored, so there is no way to see "
    #         "the user’s password."
    #     ),
    # )

    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"})
    )

    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
        "invalid_login": _(
            "Please enter a correct email and password. Note that both "
            "fields may be case-sensitive."
        ),
        "inactive": _("This account is inactive."),
    }

    class Meta:
        model = User
        fields = ['firstname', 'lastname', "nickname", "date_of_birth","email","password1","password2", "is_active", "is_staff", "is_student", "is_teacher"]
        labels = {
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'nickname': 'Nickname',
            'date_of_birth': 'Date of Birth',
            'email': 'Email',
            'is_active': 'Active',
            'is_staff': 'Staff Member',
            'is_student': 'Student',
            'is_teacher': 'Teacher'
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'border-2 w-full focus:outline-none'}),
            'is_active': forms.CheckboxInput(),
            'is_staff': forms.CheckboxInput(),
            'is_student': forms.CheckboxInput(),
            'is_teacher': forms.CheckboxInput(),
            'is_superuser': forms.CheckboxInput()
        }
        """this will help to add one by one specifically class to every field"""
        # widgets = {
        #     'username':forms.TextInput(attrs={'class':'border-2 w-full focus:outline-none'})
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # this will helps to add class on every input fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'border-2 w-full focus:outline-none'})

        # Edit password and confirm password labels
        self.fields['password1'].label = "New Password"
        self.fields['password2'].label = "Confirm New Password"

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch"
            )

        return password2

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'border-2 w-full focus:outline-none',
            'autofocus': True,
        }),
        label=_("Email")
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'border-2 w-full focus:outline-none',
            'autocomplete': 'current-password'
        }),
        label=_("Password"),
        strip=False,
    )

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'border-2 w-full focus:outline-none'})
