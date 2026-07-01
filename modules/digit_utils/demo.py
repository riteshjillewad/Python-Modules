###########################################################################################
# Name        : demo.py
# Description : Client-side to test the implemented functions
# Author      : Ritesh Jillewad
# Date        : 01-07-2026
# Version     : 1.0.0
###########################################################################################

from digit_utils import count_digits
from digit_utils import sum_digits
from digit_utils import product_digits
from digit_utils import reverse_number

def main():

    print("Enter number: ")
    num = int(input())

    ret = count_digits(num)
    print(f"Number of digits in {num}: {ret}")

    ret = sum_digits(num)
    print(f"Sum of digits of {num}: {ret}")

    ret = product_digits(num)
    print(f"Product of digits of {num}: {ret}")

    ret = reverse_number(num)
    print(f"Reversed number: {ret}")

if __name__ == "__main__":
    main()