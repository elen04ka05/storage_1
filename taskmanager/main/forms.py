from .models import Sign, Snippet
from django.forms import ModelForm, TextInput


class EmailForm(ModelForm):
    class Meta:
        model = Sign
        fields = ["username", "email", "pass_1", "pass_2"]
        widgets = {
            "username": TextInput(attrs={
                'class': 'border w-full text-base px-2 py-1 focus:outline-none focus:ring-0 focus:border-gray-600',
                'placeholder': 'Enter username'
            }),
            "email": TextInput(attrs={
                'class': 'border w-full text-base px-2 py-1 focus:outline-none focus:ring-0 focus:border-gray-600',
                'placeholder': 'Enter email'
            }),
            "pass_1": TextInput(attrs={
                'class': 'border w-full text-base px-2 py-1 focus:outline-none focus:ring-0 focus:border-gray-600',
                'placeholder': 'Enter password'
            }),
            "pass_2": TextInput(attrs={
                'class': 'border w-full text-base px-2 py-1 focus:outline-none focus:ring-0 focus:border-gray-600',
                'placeholder': 'Repeat password'
            }),
        }


class Sign_in_Form(ModelForm):
    class Meta:
        model = Sign
        fields = ["username", "pass_1"]
        widgets = {
            "username": TextInput(attrs={
                'class': 'border w-full text-base px-2 py-1 focus:outline-none focus:ring-0 focus:border-gray-600',
                'placeholder': 'Enter username'
            }),
            "pass_1": TextInput(attrs={
                'class': 'border w-full text-base px-2 py-1 focus:outline-none focus:ring-0 focus:border-gray-600',
                'placeholder': 'Enter password'
            }),
        }


class Sign_in_Email_Form(ModelForm):
    class Meta:
        model = Sign
        fields = ["email", "pass_1"]
        widgets = {
            "email": TextInput(attrs={
                'class': 'border w-full text-base px-2 py-1 focus:outline-none focus:ring-0 focus:border-gray-600',
                'placeholder': 'Enter email'
            }),
            "pass_1": TextInput(attrs={
                'class': 'border w-full text-base px-2 py-1 focus:outline-none focus:ring-0 focus:border-gray-600',
                'placeholder': 'Enter password'
            }),
        }


class Snippet_Form(ModelForm):
    model = Snippet
    fields = ["header", "code_container"]
    widgets = {
        "header": TextInput(attrs={
            'class': 'border w-full text-base px-2 py-1 focus:outline-none focus:ring-0 focus:border-gray-600',
            'placeholder': 'Name your project'
        }),
        "code_container": TextInput(attrs={
            'class': 'border w-full text-base px-2 py-1 focus:outline-none focus:ring-0 focus:border-gray-600',
            'placeholder': 'Write your project'
        }),
    }


class Profil_Edit_Form(ModelForm):
    model = Sign
    fields = ["username"]
    widgets = {"username": TextInput(attrs={
            'placeholder': 'Change your username'
        })}