from django import forms


class CreateTeamForm(forms.Form):
    name = forms.CharField(label="TeamName", max_length=30)


class CreateLeagueForm(forms.Form):
    name = forms.CharField(label="LeagueName", max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
