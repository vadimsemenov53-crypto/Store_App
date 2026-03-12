def test_order_base(object_orders):
    assert object_orders.name == "Заказ 1"
    assert object_orders.description == "Покупка телефона"
    assert object_orders.product.name == "Iphone 15"
    assert object_orders.quantity == 3

    assert object_orders.get_total_price() == 630000.0
