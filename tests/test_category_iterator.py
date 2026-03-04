import pytest

from src.category_iterator import CategoryIterator

def test_category_iterator_base(data_category):
    iterator = CategoryIterator(data_category)

    assert str(iterator.category) == 'Смартфоны, количество продуктов: 27 шт.'
    assert iterator.index == 0

    assert next(iterator) == 'Samsung Galaxy S23 Ultra'
    assert iterator.index == 1

    assert next(iterator) == 'Iphone 15'
    assert iterator.index == 2

    assert next(iterator) == 'Xiaomi Redmi Note 11'
    assert iterator.index == 3

    with pytest.raises(StopIteration):
        next(iterator)

def test_category_iterator_iter(data_category):
    iterator = CategoryIterator(data_category)

    result = []
    for i in iterator:
        result.append(i)

    assert result == ['Samsung Galaxy S23 Ultra', 'Iphone 15', 'Xiaomi Redmi Note 11']