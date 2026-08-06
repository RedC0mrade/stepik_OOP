def is_fraction(string: str) -> bool:

    some_numbers: list[str] = string.split("/")
    if len(some_numbers) != 2:
        return False

    try:
        if int(some_numbers[1]) <= 0:
            return False
    except ValueError:
        pass

    for i in some_numbers:
        try:
            float(i)
        except ValueError:
            return False

    return True


# INPUT DATA:

# TEST_1:
print("# TEST_1:", is_fraction('1000/1'))

# TEST_2:
print("# TEST_2:", is_fraction('-54/9'))

# TEST_3:
print("# TEST_3:", is_fraction('71'))

# TEST_4:
print("# TEST_4:", is_fraction('1/0'))

# TEST_5:
print("# TEST_5:", is_fraction(''))

# TEST_6:
print("# TEST_6:", is_fraction('/4'))

# TEST_7:
print("# TEST_7:", is_fraction('1000'))

# TEST_8:
print("# TEST_8:", is_fraction('-987/1'))

# TEST_9:
print("# TEST_9:", is_fraction('0/1'))

# TEST_10:
print("# TEST_10:", is_fraction('-/56'))

# TEST_11:
print("# TEST_11:", is_fraction('1/1234'))

# TEST_12:
print("# TEST_12:", is_fraction('2-/4'))

# TEST_13:
print("# TEST_13:", is_fraction('3/-7'))

# TEST_14:
print("# TEST_14:", is_fraction('5/8-'))

# TEST_15:
print("# TEST_15:", is_fraction('--1/2'))

# TEST_16:
print("# TEST_16:", is_fraction('-7/3-'))

# TEST_17:
print("# TEST_17:", is_fraction('-7-/-3-'))

# TEST_18:
print("# TEST_18:", is_fraction('/4/5'))

# TEST_19:
print("# TEST_19:", is_fraction('4/5/'))

# TEST_20:
print("# TEST_20:", is_fraction('54365486548645/472342935648904709456'))

# TEST_21:
print("# TEST_21:", is_fraction('5/2/4'))

# TEST_22:
print("# TEST_22:", is_fraction('5/2/4/2'))

# TEST_23:
print("# TEST_23:", is_fraction('1000/10'))

# TEST_24:
print("# TEST_24:", is_fraction('1000/00001'))
print("# TEST_24:", is_fraction('-1000/00001'))

# TEST_25:
print("# TEST_25:", is_fraction('1000/00004123'))
print("# TEST_25:", is_fraction('1000/0000'))
print("# TEST_25:", is_fraction('1000/00000008000'))

# OUTPUT DATA:

# # TEST_1:
# True

# # TEST_2:
# True

# # TEST_3:
# False

# # TEST_4:
# False

# # TEST_5:
# False

# # TEST_6:
# False

# # TEST_7:
# False

# # TEST_8:
# True

# # TEST_9:
# True

# # TEST_10:
# False

# # TEST_11:
# True

# # TEST_12:
# False

# # TEST_13:
# False

# # TEST_14:
# False

# # TEST_15:
# False

# # TEST_16:
# False

# # TEST_17:
# False

# # TEST_18:
# False

# # TEST_19:
# False

# # TEST_20:
# True

# # TEST_21:
# False

# # TEST_22:
# False

# # TEST_23:
# True

# # TEST_24:
# True
# True

# # TEST_25:
# True
# False
# True
