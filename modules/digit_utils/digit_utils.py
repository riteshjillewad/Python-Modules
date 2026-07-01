###########################################################################################
# Name        : digit_utils.py
# Description : Utility functions for performing various digit-based operations.
# Author      : Ritesh Jillewad
# Date        : 01-07-2026
# Version     : 1.0.0
###########################################################################################

"""
digit_utils.py

A collection of utility functions for digit-based operations.

Functions:
"""

###########################################################################################
# Basic Digit Operations
###########################################################################################

def count_digits(number):
    """
    Counts the total number of digits in a number

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    int
        Total number of digits
    """

    digitCount = 0

    if number == 0:
        return 1
    
    if number < 0:
        number = abs(number)
    
    while number != 0:
        digitCount = digitCount + 1
        number = number // 10

    return digitCount

def sum_digits(number):
    """
    Returns the sum of all digits

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    int
        Sum of digits
    """

    if number < 0:
        number = abs(number)

    while number != 0:
        digit = number % 10
        digitsSum = digitsSum + digit
        number = number // 10

    return digitsSum

def product_digits(number):
    """
    Returns the product of all digits

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    int
        Product of all digits 
    """

    if number == 0:
        return 0

    number = abs(number)
    product = 1

    while number > 0:
        digit = number % 10
        product = product * digit
        number = number // 10

    return product