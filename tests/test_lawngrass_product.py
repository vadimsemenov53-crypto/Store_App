def test_smartphone_product_base(lawngrass_obj_class):
    assert lawngrass_obj_class.name == "Газонная трава"
    assert lawngrass_obj_class.description == 'Элитная трава для газона'
    assert lawngrass_obj_class.price == 500.0
    assert lawngrass_obj_class.quantity == 20
    assert lawngrass_obj_class.country == 'Россия'
    assert lawngrass_obj_class.germination_period == '7 дней'
    assert lawngrass_obj_class.color == 'Зеленый'

    assert len(lawngrass_obj_class.list_products) == 1
    assert lawngrass_obj_class.__str__() == 'Газонная трава, 500.0 руб. Остаток: 20 шт.'