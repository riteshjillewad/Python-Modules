###########################################################################################
# Name        : demo.py
# Description : Client-side to test the implemented functions
# Author      : Ritesh Jillewad
# Date        : 01-07-2026
# Version     : 1.0.0
###########################################################################################

from number_utils import *

def main():
    num = 2

    ret = is_even(num)
    print(f"Is {num} even?: {ret}")

    ret = get_next_prime(num)
    print(f"Next prime number greater than {num}: {ret}")

if __name__ == "__main__":
    main()