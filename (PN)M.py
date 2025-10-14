import math

def is_prime(number):
    """
    Checks if a given number is a prime number.

    Args:
        number: An integer to check for primality.

    Returns:
        True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False  # Found a divisor, so it's not prime
    return True  # No divisors found, so it's prime

# Example usage:
num_to_check = 29
if is_prime(num_to_check):
    print(f"{num_to_check} is a prime number.")
else:
    print(f"{num_to_check} is not a prime number.")

num_to_check = 10
if is_prime(num_to_check):
    print(f"{num_to_check} is a prime number.")
else:
    print(f"{num_to_check} is not a prime number.")
