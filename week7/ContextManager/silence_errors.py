from contextlib import contextmanager


class silence:
    def __init__(self, error_type, *error_value):
        self.error_type = error_type
        self.error_value = error_value

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_traceback:
            if self.error_type != exc_type or self.error_value != exc_value.args:
                return False
        return True


@contextmanager
def silence_func(err_type, *message):
    try:
        yield
    except Exception as err:
        if type(err) != err_type or err.args != message:
            raise err
