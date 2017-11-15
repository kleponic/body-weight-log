from django import forms
from bodyweightlogs.models import BodyWeightLog


class BodyWeightLogForm(forms.ModelForm):
    """
    Form create or update body weightlog
    """
    class Meta:
        model = BodyWeightLog
        fields = ['date', 'max_weight', 'min_weight']

