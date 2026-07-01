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

    digitsSum = 0

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

def reverse_number(number):
    """
    Returns the reversed number

    Parameters:
    ----------------------------
    number: int 

    Returns:
    ----------------------------
    int
        Reversed number
    """

    if number == 0:
        return 0
    
    # We store the sign, so that we can handle negative numbers case
    if number < 0:
        sign = -1
    else:
        sign = 1
    
    number = abs(number)
    reverse = 0

    while number != 0:
        reverse = reverse * 10 + number % 10
        number = number // 10

    return sign * reverse

def first_digit(number):
    """
    Returns first digit from number

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    int
        First digit
    """

    if number == 0:
        return 0
    
    number = abs(number)

    # Extract the digits, until single digit is left
    while number >= 10:
        number = number // 10

    return number

def last_digit(number):
    """
    Returns the last digit from number

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    int
        Last digit
    """

    return abs(number) % 10