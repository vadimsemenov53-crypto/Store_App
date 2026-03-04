# 🛍 Store App

Учебный проект на Python для работы с категориями и товарами.

Проект реализует:
- чтение данных из JSON
- преобразование JSON в объекты
- строгую типизацию (mypy)
- unit-тестирование (pytest)
- отчёт покрытия тестами (pytest-cov)

---

## 📦 Структура проекта
```
Store_App/
│
├── src/
│ ├── product.py
│ ├── categoty.py
│ ├── utils.py
│ └── types_utils.py
│
├── tests/
│ └── test_utils.py
│
├── data/
│ └── products.json
│
├── README.md
└── main.py
```
## 🧱 Основная логика

### 🔹 Product
### Класс для представления товара:
#### Атрибуты:
- name — название товара
- description — описание
- __price — цена (приватный атрибут __price, getter и setter)
- quantity — количество на складе
#### Методы:
- new_product(dict_product: ProductDict) — classmethod для создания нового товара из словаря; если товар с таким именем существует, суммирует количество и выбирает более высокую цену
- list_products — property для получения всех товаров в виде списка объектов
- price — property с проверкой цены и подтверждением снижения через input
- clear_products() — classmethod для очистки списка товаров (используется в тестах)

### 🔹 Category
#### Класс для представления категории товаров:
##### Атрибуты:
- name — название категории
- description — описание категории
- __products: list[Product]

#### Методы:
- add_product(product: Product) — добавляет новый объект Product в категорию
- product — property, возвращает строку со списком товаров в формате:
Название продукта, Цена руб. Остаток: X шт.

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

Запуск тестов:

```bash
pytest --cov=src tests/ --cov-report=html
pytest --cov
````
````
Name                     Stmts   Miss  Cover
--------------------------------------------
src/__init__.py              0      0   100%
src/categoty.py             21      0   100%
src/product.py              37      0   100%
src/types_utils.py           3      0   100%
src/utils.py                23      0   100%
tests/__init__.py            0      0   100%
tests/conftest.py           29      0   100%
tests/test_category.py      19      0   100%
tests/test_product.py       61      0   100%
tests/test_utils.py         34      0   100%
--------------------------------------------
TOTAL                      227      0   100%
```