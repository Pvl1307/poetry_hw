import os
from unittest.mock import patch

from src.file_readers import read_csv, read_xlsx

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@patch('pandas.read_csv')
def test_read_csv(mock_read_csv):
    """Тест read_csv"""
    mock_read_csv.return_value = 'CSV data'
    result = read_csv(os.path.join(BASE_DIR, 'data', 'transactions.csv'))

    mock_read_csv.assert_called_once_with(os.path.join(BASE_DIR, 'data', 'transactions.csv'), delimiter=';')
    assert result == 'CSV data'


@patch('pandas.read_excel')
def test_read_xlsx(mock_read_excel):
    """Тест read_xlsx"""
    mock_read_excel.return_value = 'XLSX data'
    result = read_xlsx(os.path.join(BASE_DIR, 'data', 'transactions.xlsx'))

    mock_read_excel.assert_called_once_with(os.path.join(BASE_DIR, 'data', 'transactions.xlsx'))
    assert result == 'XLSX data'
