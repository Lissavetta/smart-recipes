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
         
    def add(self, name):
        if name in self._items:
            self._items[name]["quantity"] += 1
        else:
            self._items[name] = {"quantity": 1, "bought": False}
   
    def has(self, name):
        return self._normalize(name) in self._items

    def remove(self, name):
        self._items.pop(self._normalize(name), None)

    def mark_bought(self, name):
        self._items[self._normalize(name)]["bought"] = True

    def is_bought(self, name):
        return self._items[self._normalize(name)]["bought"]
    
    def get_unbought(self):
        return [name for name, info in self._items.items() if not info["bought"]]
    
    def clear(self):
        self._items.clear()
        
    @staticmethod
    def _normalize(name):
        return name.strip().lower()

    def add(self, name):
        key = self._normalize(name)
        if key in self._items:
            self._items[key]["quantity"] += 1
        else:
            self._items[key] = {"quantity": 1, "bought": False}

    def get_quantity(self, name):
        return self._items[self._normalize(name)]["quantity"]
    
    def add(self, name, quantity=1):
        key = self._normalize(name)
        if not key:
            raise ValueError("Item name cannot be empty")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if key in self._items:
            self._items[key]["quantity"] += quantity
        else:
            self._items[key] = {"quantity": quantity, "bought": False}
            
    @classmethod
    def from_recipe_suggestions(cls, suggestions):
        sl = cls()
        for suggestion in suggestions:
            for ingredient in suggestion.get("missing", []):
                sl.add(ingredient)
        return sl
    
    def to_dict(self):
        items = [
            {"name": name, **info}
            for name, info in sorted(self._items.items())
        ]
        return {
            "items": items,
            "total": len(items),
            "bought": sum(1 for i in self._items.values() if i["bought"]),
        }