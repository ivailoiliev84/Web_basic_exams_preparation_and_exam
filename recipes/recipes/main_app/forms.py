from django import forms

from recipes.core.bootsrap_mixin import BootstrapFormMixin
from recipes.main_app.models import Recipe


class RecipeForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
