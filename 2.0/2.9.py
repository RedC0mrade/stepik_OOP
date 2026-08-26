def is_integer(num) -> bool:
    try:
        return(bool(int(num)))
    except ValueError:
        return False