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
    
    def has(self, name):
        return name in self._items
    
    def remove(self, name):
        del self._items[name]
        
    def remove(self, name):
        self._items.pop(name, None)
        
    def add(self, name):
        if name in self._items:
            self._items[name]["quantity"] += 1
        else:
            self._items[name] = {"quantity": 1, "bought": False}

    def mark_bought(self, name):
        self._items[name]["bought"] = True

    def is_bought(self, name):
        return self._items[name]["bought"]
    
    def get_unbought(self):
        return [name for name, info in self._items.items() if not info["bought"]]
    
    def clear(self):
        self._items.clear()