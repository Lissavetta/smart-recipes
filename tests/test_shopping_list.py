from shopping_list import ShoppingList


def test_new_shopping_list_is_empty():
    assert len(ShoppingList()) == 0

   
def test_add_item_increases_count():
    sl = ShoppingList()
    sl.add("молоко")
    assert len(sl) == 1
    
def test_add_same_item_does_not_duplicate():
    sl = ShoppingList()
    sl.add("молоко")
    sl.add("молоко")
    assert len(sl) == 1
    
def test_get_quantity_returns_count():
    sl = ShoppingList()
    sl.add("молоко")
    sl.add("молоко")
    assert sl.get_quantity("молоко") == 2
    
def test_has_existing_item():
    sl = ShoppingList()
    sl.add("молоко")
    assert sl.has("молоко") is True


def test_has_missing_item():
    assert ShoppingList().has("хлеб") is False
    
    
def test_remove_existing_item():
    sl = ShoppingList()
    sl.add("молоко")
    sl.remove("молоко")
    assert len(sl) == 0