###########################################################################################
# Name        : demo.py
# Description : Client-side to test the implemented functions
# Author      : Ritesh Jillewad
# Date        : 01-07-2026
# Version     : 1.0.0
###########################################################################################

from number_utils import *

def main():
    num = 5

    ret = is_even(num)
    print(f"Is {num} even?: {ret}")

    ret = get_cube_root(num)
    print(f"Cube root of {num}: {ret}")

    ret = get_factors(num)
    print(f"Factors of {num}: {ret}")

    ret = get_factors_sum(num)
    print(f"Sum of factors of {num}: {ret}")

if __name__ == "__main__":
    main()