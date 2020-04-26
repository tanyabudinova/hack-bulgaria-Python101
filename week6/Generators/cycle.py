def cycle(iterable):
    while True:
        for i in iterable:
            yield i


# endless = cycle(range(0, 10))
# for item in endless:
#     print(item)
