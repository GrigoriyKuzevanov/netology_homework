import datetime
from pathlib import Path
from functools import wraps


def log_decorator(old_function):

    CACHE = {}

    @wraps(old_function)
    def new_function(*args, **kwargs):
        start = datetime.datetime.now()
        result = old_function(*args, **kwargs)
        end = datetime.datetime.now()
        work_time = end - start
        name = old_function.__name__
        CACHE['name'] = name
        CACHE['date'] = start.strftime("%d.%m.%Y")
        CACHE['time'] = start.strftime("%H:%M:%S")
        CACHE['work time (sec)'] = work_time.seconds
        CACHE['args'] = f'{args} и {kwargs}'
        CACHE['return'] = result
        with open('my_function_log.log', 'a', encoding='utf-8') as f:
            f.write(f'{CACHE}\n')
        return result

    return new_function


def path_to_log_decorator(path_to_log):
    def _log_decorator(old_function):

        CACHE = {}

        @wraps(old_function)
        def new_function(*args, **kwargs):
            start = datetime.datetime.now()
            result = old_function(*args, **kwargs)
            end = datetime.datetime.now()
            work_time = end - start
            name = old_function.__name__
            CACHE['name'] = name
            CACHE['date'] = start.strftime("%d.%m.%Y")
            CACHE['time'] = start.strftime("%H:%M:%S")
            CACHE['work time (sec)'] = work_time.seconds
            CACHE['args'] = f'{args} и {kwargs}'
            CACHE['return'] = result
            with open(path_to_log, 'a', encoding='utf-8') as f:
                f.write(f'{CACHE}\n')
            return result

        return new_function

    return _log_decorator