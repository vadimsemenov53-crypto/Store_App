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
Класс для представления товара:
- name
- description
- price
- quantity

### 🔹 Category
Класс для представления категории товаров:
- name
- description
- products: list[Product]

Дополнительно:
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
pytest --cov
````
````
Name                     Stmts   Miss  Cover
--------------------------------------------
src/__init__.py              0      0   100%
src/categoty.py              9      0   100%
src/product.py               6      0   100%
src/types_utils.py           3      0   100%
src/utils.py                24      0   100%
tests/__init__.py            0      0   100%
tests/conftest.py           21      0   100%
tests/test_category.py       7      0   100%
tests/test_product.py        9      0   100%
tests/test_utils.py         34      0   100%
--------------------------------------------
TOTAL                      113      0   100%
```