n = ["aaa", "ssss", "ddddd", "ddddd"]
print(list(filter(lambda x: len(x) == max(map(len, n)), n)))