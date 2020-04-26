def accepts(*arguments):
    def inner(func):
        def valid_arguments(*func_arguments):
            if len(arguments) != len(func_arguments):
                raise TypeError("Argument number mismatch")
            for i in range(len(arguments)):
                if type(func_arguments[i]) is not arguments[i]:
                    raise TypeError(f"Argument {func.__code__.co_varnames[i]} of say_hello is not {str(arguments[i])}!")
            return func(*func_arguments)
        return valid_arguments
    return inner
