from shopping_list import ShoppingList


def test_new_shopping_list_is_empty():
    assert len(ShoppingList()) == 0