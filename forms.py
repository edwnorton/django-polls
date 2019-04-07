from django import forms
from .core.widgets import DateTimePickerInput

class NameForm(forms.Form):
    ip = forms.CharField(label='ip', max_length=20)
    port = forms.CharField(label='port', max_length=10)
    begintime = forms.DateTimeField(
        input_formats=['%Y/%m/%d %H:%M'],
        widget=DateTimePickerInput())
    endtime = forms.DateTimeField(
        input_formats=['%Y/%m/%d %H:%M'],
        widget=DateTimePickerInput())
