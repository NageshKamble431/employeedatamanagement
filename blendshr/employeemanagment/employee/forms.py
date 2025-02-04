from django import forms
from django.db import models
from .models import *
from moderator.choices import *
import datetime
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from datetime import datetime, time, date, timedelta
min_date = date.today() - timedelta(50*365)
today = date.today() - timedelta(18*365)

min_date = date.today()
max_date = date.today() + timedelta(1 * 31)


class employee_profile(forms.ModelForm):
    maritial_status = forms.ChoiceField(choices=maritial_status, widget=forms.RadioSelect, required=True)
    gender = forms.ChoiceField(choices=gender, widget=forms.RadioSelect, required=True)

    class Meta:
        model = employeeP
        fields = '__all__'
        exclude = ['user', 'is_active']

class employee_leave_form(forms.ModelForm):
    StartDate = forms.DateField(widget=forms.DateTimeInput(format=('%Y-%m-%d'),
                                                            attrs={'class': 'form-control datepicker', 'min': min_date,
                                                                   'max': today, 'value': today, 'type': 'date'}),
                                 )
    EndDate = forms.DateField(widget=forms.DateTimeInput(format=('%Y-%m-%d'),
                                                            attrs={'class': 'form-control datepicker', 'min': min_date,
                                                                   'max': today, 'value': today, 'type': 'date'}),
                                 )
    class Meta:
        model = EmployeeLeaveCategory
        fields = '__all__'
        exclude = ['ApprovedBy', 'IsActive','IsApprove']

