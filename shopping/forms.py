from django import forms
from .models import Item, ShoppingItem

class ItemForm(forms.ModelForm):
    """Formular für neue oder zu bearbeitende Produkte."""
    class Meta:
        model = Item
        fields = ["name", "price"]

class ShoppingItemForm(forms.ModelForm):
    """Formular zum Bearbeiten eines Eintrags in der Einkaufsliste."""
    class Meta:
        model = ShoppingItem
        fields = ["item", "quantity"]  # `purchased` wird über die Checkbox getoggelt
