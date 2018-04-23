# Euclidean algorithm
# find the greatest common divisor

def greatest_common_divisor(number1, number2):
    """
        >>> greatest_common_divisor(4851, 3003)
        231
        >>> greatest_common_divisor(60, 24)
        12
    """
    while number2 != 0:
        remainder = number1 % number2
        number1 = number2
        number2 = remainder
    return number1

if __name__ == "__main__":
    import doctest
    doctest.testmod()