from django import forms


class SearchForm(forms.Form):
    title = forms.CharField(max_length=255, widget=forms.Textarea)
    author = forms.CharField(max_length=100, widget=forms.Textarea)
    year_min = forms.CharField(widget=forms.NumberInput)
    year_max = forms.CharField(widget=forms.NumberInput)
    public_data_min = forms.DateTimeField()
    data_max = forms.DateTimeField()
    where = forms.NullBooleanField()
    words = forms.CharField(max_length=255, widget=forms.Textarea)
