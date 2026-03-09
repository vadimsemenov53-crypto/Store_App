def test_smartphone_product_base(smartphone_obj_class_1):
    assert smartphone_obj_class_1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_obj_class_1.description == '256GB, Серый цвет, 200MP камера'
    assert smartphone_obj_class_1.price == 180000.0
    assert smartphone_obj_class_1.quantity == 5
    assert smartphone_obj_class_1.efficiency == 95.5
    assert smartphone_obj_class_1.model == 'S23 Ultra'
    assert smartphone_obj_class_1.memory == 256
    assert smartphone_obj_class_1.color == 'Серый'

    assert len(smartphone_obj_class_1.list_products) == 1
    assert smartphone_obj_class_1.__str__() == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.'