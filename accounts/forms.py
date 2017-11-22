from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile

class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(label='3+3=?')
    def clean_answer(self):
        if self.cleaned_data.get('answer', None) != 6:
            raise forms.ValidationError('땡~!!!')

class SignupForm(UserCreationForm):
    phone_number = forms.CharField()
    address = forms.CharField()

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)
    def save(self):
        user = super().save()
        profile = Profile.objects.create(
            user = user,
            phone_number = self.cleaned_data['address'])
        return user
