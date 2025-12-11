class InventoryManager:

    def __init__(self):
        self.inventory = {}

    def add_item(self, item_id: int, name: str, price: float, quantity: int):
        if item_id in self.inventory:
            raise ValueError(f"Товар з ID {item_id} вже існує.")
        if price <= 0 or quantity <= 0:
            raise ValueError("Ціна та кількість мають бути позитивними.")

        self.inventory[item_id] = {
            'name': name,
            'price': price,
            'quantity': quantity
        }
        return f"Товар {name} додано."

    def get_item(self, item_id: int):
        return self.inventory.get(item_id)

    def update_price(self, item_id: int, new_price: float):
        if item_id not in self.inventory:
            return "Помилка: Товар не знайдено."
        if new_price <= 0:
            raise ValueError("Нова ціна має бути позитивною.")

        self.inventory[item_id]['price'] = new_price
        return f"Ціну товару {item_id} оновлено."

    def remove_item(self, item_id: int):
        if item_id not in self.inventory:
            return "Помилка: Товар не знайдено."
        del self.inventory[item_id]
        return f"Товар {item_id} видалено."
