import pytest
from shopping_cart import ShoppingCart

def test_can_add_item_to_cart():
    cart = ShoppingCart(5) 
    cart.add("apple")
    assert cart.size() == 1

def test_when_item_added_then_cart_contains_items():
    cart = ShoppingCart(5) 
    cart.add("apple")
    assert "apple" in cart.get_items()

def test_when_more_than_max_items_should_fail():
    # we are looking for a fail
    # how to check if a test fails # Assert that a certain exception is raised
    cart = ShoppingCart(5)
    for _ in range(5):
        cart.add("apple")
    with pytest.raises(OverflowError):
        cart.add("apple")


def test_can_get_total_price():
    print("testing can get price")
    pass


