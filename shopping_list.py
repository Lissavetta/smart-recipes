class ShoppingList:
    def __init__(self):
        self._items = {}

    def __len__(self):
        return len(self._items)

    def add(self, name):
        if name in self._items:
            self._items[name]["quantity"] += 1
        else:
            self._items[name] = {"quantity": 1}

    def get_quantity(self, name):
        return self._items[name]["quantity"]