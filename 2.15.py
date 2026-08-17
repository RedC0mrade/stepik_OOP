def recviz(func):
    print("->")
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
    return wrapper
    print("<-")




@recviz
def add(a, b):
    return a + b

add(1, b=2)