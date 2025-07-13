import time
from typing import Any, Callable, Optional


def add_logfile(filename: Optional[str]=None) ->  Callable[[Callable[..., Any]], Callable[..., Any]]:
    '''Декоратор автоматически логирует начало и конец выполнения функции,
     а также ее результаты или возникшие ошибки'''
    def log(logger: Callable[..., Any]) -> Callable[..., Any]:
        def new_param(*args: Any, **kwargs: Any) -> Any:
            try:
                time_1 = time.time()
                logger(*args, **kwargs)
                time_2 = time.time()
            except Exception as error:
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f'{logger.__name__} error: {error}.  input: {args}, {kwargs}\n')
                else:
                    print(f'{logger.__name__} error: {error}.  input: {args}, {kwargs}\n')
            else:
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f'{logger.__name__} ok, start time: {time_1}, finish time: {time_2}\n')
                else:
                    print(f'{logger.__name__} ok, start time: {time_1}, finish time: {time_2}\n')
        return new_param
    return log
