from django import forms
from django.forms import ModelForm
from .models import Todo


class DateInput(forms.DateInput):
    input_type = 'date'


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = fields = "__all__"
        widgets = {
            'deadline': DateInput(),
        }
