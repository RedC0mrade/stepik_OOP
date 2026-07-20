def bracket(string: str) -> bool:
    flag = 0
    dictionary = {'(': 1, ')': -1}
    for i in string:
        flag += dictionary[i]
        if flag < 0:
            return False
    if flag != 0:
        return False
    return True

print(bracket(string=input()))