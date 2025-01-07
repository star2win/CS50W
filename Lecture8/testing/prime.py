import math
def is_prime(n):
    """Determines if a non-negative integer is prime."""

    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))):  # intentional error, missing last value to test
        if n % i == 0:
            return False
    return True