import datetime


def logger(old_function):
    start = datetime.datetime.now()

    def new_function(*args, **kwargs):

        wrapping_start = (f'Сейчас будут вызвана функция {old_function.__name__}'
                    f' с аргументам {args} и {kwargs}')
        result = old_function(*args, **kwargs)
        wrapping_end = f'Pезультат: {result}'
        finish = datetime.datetime.now()
        working_time = finish - start
        with open('main.log', 'a', encoding='UTF-8') as f:
            f.write(f'{wrapping_start}\nВремя работы функции {old_function.__name__}:'
                    f' {working_time}\n{wrapping_end}\n\n')
        return result
    return new_function
