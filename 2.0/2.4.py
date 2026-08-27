import sys

pokemons: dict[str:int] = dict()

for i in sys.stdin:
    key = i.strip()
    pokemons[key] = pokemons.setdefault(key, -1) + 1
    print(pokemons)

print(sum(pokemons.values()))
