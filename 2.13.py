def annual_return(
    deposit: int,
    persent: int,
    years: int,
):
    if years != 0:
        yield annual_return(deposit=deposit, persent=persent, years=years-1)
    yield deposit  / 11 / persent

for value in annual_return(120000, 10, 3):
    print(round(value))