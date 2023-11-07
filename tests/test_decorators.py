import os

from src.decorators import log

log_directory = '../'


@log(filename='mylog.txt')
def my_func(x: int, y: int) -> int:
    return x + y


def test_log_decorator_ok() -> None:
    """Тест на проверку декоратора с успехом"""
    result = my_func(1, 2)

    log_path = os.path.join(log_directory, 'mylog.txt')

    with open(log_path, 'r', encoding='utf-8') as f:
        logs = f.read()

    assert result == 3
    assert 'my_func ok' in logs


def test_log_decorator_error() -> None:
    """Тест на проверку декоратора с ошибкой"""
    result = my_func(1, '2')

    log_path = os.path.join(log_directory, 'mylog.txt')

    with open(log_path, 'r', encoding='utf-8') as f:
        logs = f.read()

    assert result is None
    assert 'my_func error: TypeError unsupported operand type(s) for +:' in logs
