def silence(file_name):
    def inner(func):
        def silencing(*argv):
                try:
                    func(*argv)
                except Exception as err:
                    with open(file_name, 'w') as f:
                        message = "Calling {} raised an error - {}: '{}'. Provided arguments: {}."
                        f.write(message.format(func.__code__.co_name, type(err).__name__, err, argv))
        return silencing
    return inner


@silence('errors.txt')
def foo(x):
    if x > 50:
        raise ValueError('Omg.')


foo(10)
foo(100)
