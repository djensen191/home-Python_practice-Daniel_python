# A simple Python3 script to take a user entered range and 
# Output the prime numbers within that range.

import sys

# Take input from the user
user_input= input('Enter a lower bound and upper bound separated by a space: ')
# Split the input string into pieces by spaces
user_input = user_input.split()
# Ensure user entered a valid range.  Otherwise exit with error
if len(user_input)>2:
    sys.exit('Error! You entered an invalid range.')

values = []
# Loop over the range from 0-2 to append the values to a list
for i in range(0, 2):
    values.append(int(user_input[i]))


# Define a function that given a lower bound and an upper bound 
# Prints the prime numbers in that range
# Input: The upper and lower bounds
# Output: Prints the prime values from within the function.  (Has no return value.)
def check_prime(lower_bound, upper_bound):

    # Loop over the given range from lower bound to upper bound
    for test_value in range(lower_bound, upper_bound):
        # Loop over the numbers from 2-Current value being tested 
        for factorization in range (2, test_value):
            # Test if the current test_value mod current factorization value has a remainder of 0. 
            # If so break the number cannot be prime.
            if test_value % factorization == 0:
                break
        else:
            # Otherwise print the number is prime.
            print(f'{test_value} is Prime!')

# 
check_prime(values[0], values[1])
