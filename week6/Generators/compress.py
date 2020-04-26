def compress(iterable, mask):
    if len(iterable) != len(mask):
        raise ValueError("Different lenghts")
    for i in range(len(iterable)):
        if mask[i]:
            yield iterable[i]
