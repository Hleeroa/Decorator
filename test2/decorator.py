import datetime
from functools import wraps


def logger(path):
    def __logger(old_function):
        start = datetime.datetime.now()

        @wraps(old_function)
        def new_function(*args, **kwargs):

            wrapping_start = (f'Сейчас будут вызвана функция {old_function.__name__}'
                              f' с аргументам {args} и {kwargs}')
            result = old_function(*args, **kwargs)
            wrapping_end = f'Pезультат: {result}'
            finish = datetime.datetime.now()
            working_time = finish - start
            with open(path, 'a', encoding='UTF-8') as f:
                f.write(f'{wrapping_start}\nВремя работы функции {old_function.__name__}:'
                        f' {working_time}\n{wrapping_end}\n\n')
            return result
        return new_function
    return __logger
