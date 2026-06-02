import multiprocessing
import math
import sys
import time

sys.set_int_max_str_digits(100000)

def compute_factorial(number):
    print(f"Factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")

if __name__ == '__main__':
    numbers = [6000, 7000, 8000]

    start_time = time.time()

    with multiprocessing.Pool() as pool:
        # Map the compute_factorial function to the list of numbers
        results = pool.map(compute_factorial, numbers)
    
    end_time = time.time()

    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")