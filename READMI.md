# 🛍 Store App

Учебный проект на Python для работы с категориями и товарами.

Проект реализует:
- чтение данных из JSON
- преобразование JSON в объекты
- строгую типизацию (mypy)
- unit-тестирование (pytest)
- отчёт покрытия тестами (pytest-cov)

---

## 🧱 Архитектура проекта

Проект построен с использованием принципов **объектно-ориентированного программирования (OOP)**  
и включает:

- абстрактные базовые классы
- наследование
- миксины
- магические методы
- строгую типизацию
- unit-тестирование

## 🧱 Основная логика

## Абстрактный базовый класс для продуктов
Создан абстрактный класс `BaseProduct`, который определяет общий интерфейс для всех товаров.

```python
from abc import ABC, abstractmethod

class BaseProduct(ABC):
    price: float
    quantity: int

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> float:
        pass
```

### Миксин для вывода информации о создании объектов
Добавлен миксин PrintMixin, который выводит информацию о создаваемом объекте при его инициализации.
```python
class PrintMixin:
    def __init__(self) -> None:       
        print(repr(self))

    def __repr__(self) -> str:
        obj: Any = self
        return f"{obj.__class__.__name__} ({obj.name}, {obj.description}, {obj.price}, {obj.quantity})"
```
Пример: Product (Iphone 15, 512GB, Gray space, 210000.0, 8)

### 🔹 Product
### Класс для представления товара:
#### Атрибуты:
- name — название товара
- description — описание
- __price — цена (приватный атрибут __price, getter и setter)
- quantity — количество на складе
- 
#### Методы:
- new_product(dict_product: ProductDict) — classmethod для создания нового товара из словаря; если товар с таким именем существует, суммирует количество и выбирает более высокую цену
- list_products — property для получения всех товаров в виде списка объектов
- price — property с проверкой цены и подтверждением снижения через input
- clear_products() — classmethod для очистки списка товаров (используется в тестах)
- str - Возвращает название категории и общее количество товаров (с учётом их количества).
- product_list - Позволяет получить список объектов Product. Поддерживает использование в for.
- Магический метод __add__ - Для товаров реализован оператор сложения +. Метод возвращает общую стоимость двух товаров с учётом их количества.
```dockerfile
__add__ -> 
Метод работает только для объектов одного типа:
Smartphone + Smartphone
LawnGrass + LawnGrass
При попытке сложить разные типы будет выброшено исключение TypeError.
```
### 📦 Наследование товаров
В проекте реализованы специализированные типы товаров через механизм наследования.
Базовым классом является Product, от которого наследуются конкретные типы товаров.

### Smartphone
Класс для представления смартфонов.

#### Дополнительные атрибуты:
- efficiency — производительность
- model — модель устройства
- memory — объём памяти
- color — цвет устройства

#### Пример создания:
```pythonverboseregexp
phone = Smartphone(
    "iPhone 15",
    "512GB",
    210000.0,
    8,
    98.5,
    "A3102",
    512,
    "Gray"
)
```

### LawnGrass
Класс для представления газонной травы.

#### Дополнительные атрибуты:
- country — страна производства
- germination_period — срок всхода
- color — цвет травы

#### Пример создания:
```pythonverboseregexp
grass = LawnGrass(
    "Газонная трава",
    "Семена для газона",
    500.0,
    20,
    "Нидерланды",
    "7-10 дней",
    "Зелёный"
)
```

## Абстрактная модель для бизнес-сущностей
Создан базовый абстрактный класс BaseModel, который используется для классов Category и Order.

```python
from abc import ABC, abstractmethod

class BaseModel(ABC):

    name: str
    description: str

    @abstractmethod
    def get_total_price(self):
        pass
```
Этот класс задаёт общий интерфейс для получения общей стоимости.

### 🔹 Order - Класс заказа
#### Добавлен класс Order, который представляет заказ пользователя.
### Особенности:
- заказ содержит ссылку на товар (Product)
- хранит количество купленного товара
- умеет рассчитывать итоговую стоимость заказа

### 🔹 Category
#### Класс для представления категории товаров:
##### Атрибуты:
- name — название категории
- description — описание категории
- __products: list[Product]

#### Методы:
- add_product(product: Product) — Метод позволяет добавлять в категорию только объекты класса Product или его наследников.
- product — property, возвращает строку со списком товаров в формате:
Название продукта, Цена руб. Остаток: X шт.
- str - Отображает название, цену и остаток товара
- add - Позволяет складывать общую стоимость двух товаров с учётом их количества
- get_total_price, который вычисляет общую стоимость всех товаров категории.

#### add_product:
```dockerfile
Для проверки используется функция isinstance().
Она позволяет убедиться, что переданный объект является:

объектом класса Product

или объектом класса-наследника (Smartphone, LawnGrass и др.)

Если попытаться добавить любой другой объект, будет вызвано исключение TypeError.

Пример:

category.add_product(Smartphone(...))   # работает
category.add_product(LawnGrass(...))    # работает
category.add_product("строка")          # TypeError
```

#### Атрибуты класса:
- category_count — количество созданных категорий
- all_products_count — общее количество товаров
---

## 📥 Чтение JSON

Функция `read_json()`:
- читает JSON-файл
- возвращает `list[CategoryDict]`
- использует `TypedDict`
- проходит строгую проверку `mypy`

---

## 🔄 Преобразование данных

Функция `create_obj_from_json()`:
- принимает список словарей
- создаёт объекты `Product`
- создаёт объекты `Category`
- возвращает `list[Category]`

---

## 🧪 Тестирование

Используется:
- pytest
- unittest.mock
- фикстуры
- проверка исключений
- изоляция тестов (сброс счётчиков)
- Проверяются: 
1. Итераторы 
2. Магические методы (__str__, __add__)
3. Геттеры и сеттеры 
4. Логика подтверждения изменения цены 
5. Граничные случаи

Запуск тестов:

```bash
pytest --cov=src tests/ --cov-report=html
pytest --cov
````
````
Name                               Stmts   Miss  Cover
------------------------------------------------------
src/__init__.py                        0      0   100%
src/base_model.py                      5      1    80%
src/base_product.py                    6      1    83%
src/category_iterator.py              14      0   100%
src/categoty.py                       32      0   100%
src/lawngrass_product.py              12      0   100%
src/order.py                          10      0   100%
src/print_mixin.py                     8      0   100%
src/product.py                        46      0   100%
src/smartphone_product.py             13      0   100%
src/types_utils.py                     3      0   100%
src/utils.py                          23      0   100%
tests/__init__.py                      0      0   100%
tests/conftest.py                     51      0   100%
tests/test_category.py                37      0   100%
tests/test_category_iterator.py       20      0   100%
tests/test_lawngrass_product.py       18      0   100%
tests/test_order.py                    6      0   100%
tests/test_print_mixin.py             13      0   100%
tests/test_product.py                 90      0   100%
tests/test_smartphone_product.py      19      0   100%
tests/test_utils.py                   34      0   100%
------------------------------------------------------
TOTAL                                460      2    99%
```