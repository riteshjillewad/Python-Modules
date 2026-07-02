###########################################################################################
# Name        : demo.py
# Description : Client-side to test the implemented functions
# Author      : Ritesh Jillewad
# Date        : 01-07-2026
# Version     : 1.0.0
###########################################################################################

from digit_utils import *

def main():

    num = 18

    ret = count_digits(num)
    print(f"Number of digits in {num}: {ret}")

# <-----    ADD MORE FUNCTIONS FOR TESTING     ------>

    ret = is_harshad(num)
    if ret == True:
        print(f"{num} is harshad number")
    else:
        print(f"{num} is not harshad number")

if __name__ == "__main__":
    main()