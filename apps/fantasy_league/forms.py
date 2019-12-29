from django import forms


class CreateTeamForm(forms.Form):
    name = forms.CharField(label="TeamName", max_length=30)
