def is_cpr(sample):
    # has the length 6
    if len(sample) != 6:
        return False

    # are all digits
    for char in sample:
        if not char.isdigit():
            return False

    # first 2 digits must be between 01 and 52

    first_two_digits = int(sample[:2])
    if first_two_digits < 1 or first_two_digits > 52:
        return False

    # is cpr

    return True

print(is_cpr("123456"))