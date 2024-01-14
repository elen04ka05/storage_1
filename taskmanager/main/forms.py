from .models import Sign, Create
from django.forms import ModelForm, TextInput, Textarea, DateInput, Select


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


class Profil_Edit_Form(ModelForm):
    model = Sign
    fields = ["username"]
    widgets = {"username": TextInput(attrs={
            'placeholder': 'Change your username'
        })}


class CreateForm(ModelForm):
    class Meta:
        model = Create
        fields = ["filename", "code", "date", "lang"]
        widgets = {
            "filename": TextInput(attrs={
                'class': 'p-1 border w-1/5 text-base focus:outline-none focus:ring-0 focus:border-gray-600 border-rounded-lg',
                'placeholder': 'Filename'
            }),
            "code": Textarea(attrs={
                'class': 'w-full px-0 text-sm text-gray-900 bg-white border-2 border-rounded-lg border-blue-500 dark:bg-gray-800 focus:ring-3 dark:text-white dark:placeholder-gray-400',
                'placeholder': 'Enter code'
            }),
            "date": DateInput(attrs={
                'class': 'p-2',
                'placeholder': 'Creation date'
            }),
            "lang": Select(attrs={
                'class': 'p-2',
                'placeholder': 'Select language'
            })
        }