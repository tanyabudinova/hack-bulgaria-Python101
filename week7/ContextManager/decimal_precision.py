import decimal


class change_precision:
    def __init__(self, precision):
        decimal.getcontext().prec = precision

    def __enter__(self):
        pass

    def __exit__(self, type, vale, trace_back):
        pass
