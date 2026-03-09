def test_smartphone_product_base(smartphone_obj_class):
    assert smartphone_obj_class.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_obj_class.description == '256GB, Серый цвет, 200MP камера'
    assert smartphone_obj_class.price == 180000.0
    assert smartphone_obj_class.quantity == 5
    assert smartphone_obj_class.efficiency == 95.5
    assert smartphone_obj_class.model == 'S23 Ultra'
    assert smartphone_obj_class.memory == 256
    assert smartphone_obj_class.color == 'Серый'

    assert len(smartphone_obj_class.list_products) == 1
    assert smartphone_obj_class.__str__() == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.'