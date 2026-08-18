def recviz(func):
    print("->")
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'вызов {func.__name__}() с аргументами: {args}, {kwargs}')
        print(f'TRACE: возвращаемое значение {func.__name__}(): {repr(result)}')

    return wrapper




@recviz
def add(a, b):
    return a + b

add(1, b=2)

# -> add(1, b=2)
# <- 3
