from django import forms


class CreateTeamForm(forms.Form):
    name = forms.CharField(label="TeamName", max_length=30)


class ChoosePlayer(forms.Form):
    player = forms.CharField(label="PlayerName", max_length=50)
