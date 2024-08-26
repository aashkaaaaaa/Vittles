from django import forms
from .views import get_ingreds_from_csv

csv_file_path = 'testapp/data/ingriedEng.csv'

class IngredientForm(forms.Form):
    ingredients = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=get_ingreds_from_csv(csv_file_path),
        label='Select Ingredients',
    )
