from django import forms
from .models import Review
from .models import CallBack


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'firstname',
            'lastname',
            'stars',
            'description',
        ]


class CallBackForm(forms.ModelForm):
    class Meta:
        model = CallBack
        fields = [
            'email',
            'number',
            'message'
        ]