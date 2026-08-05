def intersperse(iterable, delimiter):
    iterator = list(iterable)
    if iterator:
        for i in iterator[:-1]:
            yield i
            yield delimiter
        yield iterator[-1]



