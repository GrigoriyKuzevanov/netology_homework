from decorators import log_decorator, path_to_log_decorator
from pathlib import Path


@log_decorator
def some_function(*args, **kwargs):
    res = 'Function was called'
    return res


some_function(1, arg=None)

path = Path(Path.cwd(), 'my_log.log')


@path_to_log_decorator(path)
def my_function(*args, **kwargs):
    res = 'my_function was called'
    return res

my_function()

