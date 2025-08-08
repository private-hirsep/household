from django.urls import path
from .views import *

urlpatterns = [
    path("", ShoppingListView.as_view(), name="shopping-list"),
    path("item/add/", ItemCreateView.as_view(), name="item-add"),
    path("item/<int:pk>/", ItemDetailView.as_view(), name="item-detail"),
    path("item/<int:pk>/edit/", ItemUpdateView.as_view(), name="item-edit"),
    path("shoppingitem/<int:pk>/edit/", ShoppingItemUpdateView.as_view(), name="shoppingitem-edit"),
    path("shoppingitem/<int:pk>/delete/", ShoppingItemDeleteView.as_view(), name="shoppingitem-delete"),
    path("shoppingitem/<int:pk>/toggle/", toggle_shopping_item, name="shoppingitem-toggle"),
    path("items/", ItemListView.as_view(), name="item-list"),
    path("item/<int:pk>/delete/", ItemDeleteView.as_view(), name="item-delete"),
    path("clear/", ClearShoppingListView.as_view(), name="shopping-clear"),
]
