from src.order import Order

def test_order_base(object_orders):
    assert object_orders.name == "Заказ 1"
    assert object_orders.description == "Покупка телефона"
    assert object_orders.product.name == "Iphone 15"
    assert object_orders.quantity == 3

    assert object_orders.get_total_price() == 630000.0


def test_order_base_consol(capsys, object_orders):
    message = capsys.readouterr()

    assert message.out.strip().split('\n')[-3] == 'Smartphone (Iphone 15, 512GB, Gray space, 210000.0, 8)'
    assert message.out.strip().split('\n')[-2] == 'Товар добавлена успешно.'
    assert message.out.strip().split('\n')[-1] == 'Обработка добавления товара прошла успешно.'


def test_order_error_consol(capsys, smartphone_obj_class_1):
    Order('test', 'test', smartphone_obj_class_1, 0)

    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-3] == ('Smartphone '
                                                   '(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)')
    assert message.out.strip().split('\n')[-2] == 'ZeroProductQuantity: Нельзя оформить заказ с нулевым количеством товара.'
    assert message.out.strip().split('\n')[-1] == 'Обработка добавления товара прошла успешно.'
