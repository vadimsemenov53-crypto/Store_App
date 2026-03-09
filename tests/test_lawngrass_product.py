def test_smartphone_product_base(lawngrass_obj_class_1):
    assert lawngrass_obj_class_1.name == "Газонная трава"
    assert lawngrass_obj_class_1.description == 'Элитная трава для газона'
    assert lawngrass_obj_class_1.price == 500.0
    assert lawngrass_obj_class_1.quantity == 20
    assert lawngrass_obj_class_1.country == 'Россия'
    assert lawngrass_obj_class_1.germination_period == '7 дней'
    assert lawngrass_obj_class_1.color == 'Зеленый'

    assert len(lawngrass_obj_class_1.list_products) == 1
    assert (lawngrass_obj_class_1.__str__() == 'Газонная трава, 500.0 руб. Остаток: 20 шт.')