a = ['o', 'to', 'otto', 'top', 't']

b = ['o', 't']

for i in a:
    print(set(i).isdisjoint(set(b)))