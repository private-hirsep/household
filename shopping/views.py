from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView,
)
from .models import Item, ShoppingItem
from .forms import ItemForm, ShoppingItemForm
from django.views import View

class ShoppingListView(ListView):
    """Liste der ShoppingItems mit Suchfeld und Summen."""
    model = ShoppingItem
    template_name = "shopping/shopping_list.html"
    context_object_name = "shopping_items"
    ordering = ["purchased", "id"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_items"] = Item.objects.all()  # Vorschläge im datalist
        total_quantity = sum(item.quantity for item in context["shopping_items"])
        total_price = sum(item.get_total_price() for item in context["shopping_items"])
        context["total_quantity"] = total_quantity
        context["total_price"] = total_price
        return context

    def post(self, request, *args, **kwargs):
        """Neuen Eintrag über das Suchfeld hinzufügen."""
        item_name = request.POST.get("item_name")
        quantity_value = request.POST.get("quantity")
        try:
            quantity = int(quantity_value) if quantity_value else 1
        except (TypeError, ValueError):
            quantity = 1
        if item_name:
            try:
                item = Item.objects.get(name__iexact=item_name.strip())
                ShoppingItem.objects.create(item=item, quantity=quantity)
            except Item.DoesNotExist:
                messages.error(
                    request,
                    f'Item "{item_name}" not found. Please add it first using the + button.',
                )
        return redirect("shopping-list")

class ShoppingItemUpdateView(UpdateView):
    model = ShoppingItem
    form_class = ShoppingItemForm
    template_name = "shopping/shopping_item_form.html"
    success_url = reverse_lazy("shopping-list")

class ShoppingItemDeleteView(DeleteView):
    model = ShoppingItem
    template_name = "shopping/shopping_item_confirm_delete.html"
    success_url = reverse_lazy("shopping-list")

@require_POST
def toggle_shopping_item(request, pk):
    """Kauftstatus umschalten und zurück zur Liste."""
    shopping_item = get_object_or_404(ShoppingItem, pk=pk)
    shopping_item.purchased = not shopping_item.purchased
    shopping_item.save()
    return redirect("shopping-list")

class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = "shopping/item_form.html"
    success_url = reverse_lazy("shopping-list")

class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = "shopping/item_form.html"

    def get_success_url(self):
        return reverse_lazy("item-detail", kwargs={"pk": self.object.pk})

class ItemDetailView(DetailView):
    model = Item
    template_name = "shopping/item_detail.html"
    context_object_name = "item"

class ItemListView(ListView):
    """Zeigt alle Artikel mit Edit‑ und Delete‑Aktionen."""
    model = Item
    template_name = "shopping/item_list.html"
    context_object_name = "items"
    ordering = ["name"]

class ItemDeleteView(DeleteView):
    """Bestätigt und entfernt einen Artikel."""
    model = Item
    template_name = "shopping/item_confirm_delete.html"
    success_url = reverse_lazy("item-list")

class ClearShoppingListView(View):
    def post(self, request, *args, **kwargs):
        ShoppingItem.objects.filter(purchased=True).delete()
        return redirect('shopping-list')
    
