import os
from datetime import date, datetime
from functools import wraps
from typing import Callable, Optional, Any

log_directory = '../'


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования выполнения функций."""

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                status = 'ok'
            except Exception as e:
                result = None
                status = f'error: {type(e).__name__} {str(e)}. Inputs: {args}, {kwargs}'

            info = f'{date.today()} {datetime.now().strftime("%H:%M:%S")} {func.__name__} {status}'

            if filename:
                log_path = os.path.join(log_directory, filename)
                with open(log_path, 'a', encoding='utf-8') as f:
                    f.write(f'{info}\n')
            else:
                print(info)

            return result

        return inner

    return wrapper
