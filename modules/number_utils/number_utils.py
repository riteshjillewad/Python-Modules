###########################################################################################
# Name        : digit_utils.py
# Description : Utility functions for performing various digit-based operations.
# Author      : Ritesh Jillewad
# Date        : 01-07-2026
# Version     : 1.0.0
###########################################################################################

"""
number_utils.py
A collection of utility functions for number-based (whole numbers) operations

Functions:

"""

###########################################################################################
# Basic Number Operations
###########################################################################################

def is_even(number: int) -> bool:
    """
    Returns true if number is even

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    bool:
        True or false
    """

    """
    Alternate approach: Bitwise operations
        Ex: 6(0110), 7(0111)
        - number & 1 == 0 (LSB 0 means no odd value is present)
        - number & 1 == 1 (LSB 1 means there is remainder of 1)
    """
    # return number % 2 == 0
    return number & 1 == 0

def is_odd(number: int) -> bool:
    """
    Returns true if number is odd

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    bool:
        True or false
    """
    
    return number & 1 != 0

def square_num(number: int) -> int:
    """
    Returns the square of the number

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    int:
        Square of number
    """

    return number ** 2

def cube_num(number: int) -> int:
    """
    Returns the cube of number

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    int:
        Cube of number
    """

    return number ** 3

def power_num(base: int, exponent: int) -> int:
    """
    Returns the power value of number

    Parameters:
    ------------------------------
    base: int
    exponent: int

    Return value:
    ------------------------------
    int:
        Power value of number
    """

    return base ** exponent

def get_square_root(number: int | float) -> float:
    """
    Returns the square root of number

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    int:
        Square root of number
    """

    if number < 0:
        raise ValueError("Cannot find square root of negative number")

    return number ** 0.5

def get_cube_root(number: int | float) -> float:
    """
    Returns the cube root of number

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    int:
        Cube root of number
    """

    if number < 0:
        raise ValueError("Cannot find cube root of negative number")

    return number ** (1/3)

def get_factors(number: int) -> list[int]:
    """
    Returns the factors of the number
    
    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    list[int]:
        Factors of number
    """

    if number <= 0:
        raise ValueError("Factors are calculated for positive integers greater than 0.")

    factors = set()

    for i in range(1, int(get_square_root(number)) + 1):
        if number % i == 0:
            factors.add(i)
            factors.add(number // i)

    return sorted(list(factors))

def get_factors_count(number: int) -> int:
    """
    Returns the count of factors of number

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    int:
        count of factors
    """

    fact_count = 0

    if number <= 0:
        raise ValueError("Factors are calculated for positive integers greater than 0.")
    
    for i in range(1, int(get_square_root(number)) + 1):
        if number % i == 0:
            # If the factors are distinct pairs (e.g., 2 and 6 for 12), add 2
            if i * i != number:
                fact_count += 2
            # If it's a perfect square root (e.g., 5 and 5 for 25), only add 1
            else:
                fact_count += 1

    return fact_count

def get_factors_sum(number: int) -> int:
    """
    Returns the sum of factors 

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    int:
        sum of factors
    """

    return sum(get_factors(number))