def chain(iterable1, iterable2):
    for i in iterable1:
        yield i

    for i in iterable2:
        yield i


print(set(chain(range(0, 4), range(4, 8))))
