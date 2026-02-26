from json import JSONDecodeError
from unittest.mock import patch
from src.utils import read_json, create_obj_from_json
from src.categoty import Category

@patch("src.utils.json.load")
def test_read_json_base(mock_json, data_for_json_read, tmp_path):
    mock_json.return_value = data_for_json_read

    file_path = tmp_path / 'test.json'
    file_path.write_text('{}', encoding='utf-8')

    assert read_json(str(file_path)) == data_for_json_read

    mock_json.assert_called_once()

@patch("src.utils.json.load")
@patch("src.utils.os.path.join")
def test_read_json_base_path(mock_path, mock_json, data_for_json_read, tmp_path):
    mock_json.return_value = data_for_json_read

    assert read_json() == data_for_json_read

    mock_path.assert_called_once()
    mock_json.assert_called_once()


@patch("src.utils.json.load")
def test_read_json_wrong_json(mock_json, tmp_path):
    mock_json.side_effect = JSONDecodeError("", "", 0)

    file_path = tmp_path / 'test.json'
    file_path.write_text('{}', encoding='utf-8')

    assert read_json(str(file_path)) == []

    mock_json.assert_called_once()


def test_create_obj_from_json(data_for_json_read):
    Category.category_count = 0
    Category.product_count = 0

    result = create_obj_from_json(data_for_json_read)

    assert result[0].name == 'Смартфоны'
    assert result[0].description == 'Мобильные устройства'
    assert len(result[0].products) == 1

    assert result[0].category_count == 1
    assert result[0].product_count == 1