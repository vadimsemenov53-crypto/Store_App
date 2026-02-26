from src.categoty import Category

def test_category_base(data_category):
    assert data_category.name == 'Смартфоны'
    assert (data_category.description ==
            'Средства не только коммуникации, но и получения дополнительных функций для удобства жизни')
    assert len(data_category.products) == 3

    assert Category.category_count == 1
    assert Category.all_products_count == 3