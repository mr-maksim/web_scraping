from datetime import datetime
from functools import wraps
import os


def logger(path):
    def _logger(old_function):
        if not os.path.exists(path):
            os.makedirs(path)

        @wraps(old_function)
        def new_function(*args, **kwargs):
            start = datetime.now()
            result = old_function(*args, **kwargs)
            end = datetime.now()
            term = '*'*30
            log = f'{term}\n{start} - Function: {old_function.__name__} called {args,kwargs}.\nReturn:{result}.\nWorking time {end-start}.\n{term}\n\n'
            with open(f'{path}/log.txt', 'a') as file:
                file.write(log)
            return result
        return new_function
    return _logger
