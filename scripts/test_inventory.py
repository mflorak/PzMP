import pytest
from scripts.inventory import InventoryManager


@pytest.fixture
def inventory_setup():
    manager = InventoryManager()
    manager.add_item(1, "Laptop", 1200.00, 5)
    manager.add_item(2, "Mouse", 25.00, 10)
    return manager



def test_add_item_success(inventory_setup):
    manager = inventory_setup
    result = manager.add_item(3, "Keyboard", 75.00, 3)
    assert result == "Товар Keyboard додано."
    assert 3 in manager.inventory
    assert manager.inventory[3]['price'] == 75.00


def test_add_item_duplicate_id(inventory_setup):
    manager = inventory_setup
    with pytest.raises(ValueError) as excinfo:
        manager.add_item(1, "Duplicate Laptop", 100.00, 1)
    assert "Товар з ID 1 вже існує" in str(excinfo.value)


def test_add_item_invalid_price(inventory_setup):
    manager = inventory_setup
    with pytest.raises(ValueError) as excinfo:
        manager.add_item(4, "Bad Item", -10.00, 5)
    assert "Ціна та кількість мають бути позитивними" in str(excinfo.value)



def test_get_item_existing(inventory_setup):
    manager = inventory_setup
    item = manager.get_item(2)
    assert item is not None
    assert item['name'] == "Mouse"


def test_get_item_non_existing(inventory_setup):
    manager = inventory_setup
    item = manager.get_item(99)
    assert item is None



def test_update_price_success(inventory_setup):
    manager = inventory_setup
    manager.update_price(1, 1300.50)
    assert manager.inventory[1]['price'] == 1300.50


def test_update_price_item_not_found(inventory_setup):
    manager = inventory_setup
    result = manager.update_price(99, 100.00)
    assert result == "Помилка: Товар не знайдено."


def test_update_price_invalid_price(inventory_setup):
    manager = inventory_setup
    with pytest.raises(ValueError) as excinfo:
        manager.update_price(1, 0)
    assert "Нова ціна має бути позитивною" in str(excinfo.value)


# --- Тести для методу remove_item ---

def test_remove_item_success(inventory_setup):
    manager = inventory_setup
    result = manager.remove_item(1)
    assert result == "Товар 1 видалено."
    assert 1 not in manager.inventory


def test_remove_item_non_existing(inventory_setup):
    manager = inventory_setup
    result = manager.remove_item(99)
    assert result == "Помилка: Товар не знайдено."