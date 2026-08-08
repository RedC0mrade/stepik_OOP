def annual_return(
    deposit: int,
    persent: int,
    years: int,
):

    for _ in range(years):
       deposit = deposit * (100 + persent) / 100
       yield deposit
    
for value in annual_return(120000, 10, 3):
    print(round(value))

for value in annual_return(70000, 8, 10):
    print(round(value))