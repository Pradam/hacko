from django import forms
from .models import HistoryData

class HistoryDataForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HistoryDataForm, self).__init__(*args, **kwargs)
        self.fields['gender'].widget.attrs['class'] = 'form-control'
        self.fields['is_smoker'].widget.attrs['class'] = 'form-control'
        self.fields['is_alcoholic'].widget.attrs['class'] = 'form-control'
        self.fields['claimed'].widget.attrs['class'] = 'form-control'
        self.fields['is_member'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = HistoryData
        fields = ('aadhar_id', 'name',
                  'gender', 'age',
                  'coverage',
                  'is_alcoholic','is_smoker',
                  'claimed', 'is_member')



