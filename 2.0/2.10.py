def is_decimal(num) -> bool:
    try:
        return(bool(float(num)))
    except ValueError:
        return False