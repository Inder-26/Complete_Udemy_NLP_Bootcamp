### Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(1)
    return f"Sqaure: {number * number}"

number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

if __name__ == "__main__":

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number,number)

    for result in results:
        print(result)