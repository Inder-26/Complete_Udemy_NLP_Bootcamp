import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")

def print_letters():
    for letter in "ABCD":
        time.sleep(2)
        print(f"Letter: {letter}")

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)
    
start_time = time.time()

## Start the thread
t1.start()
t2.start()

t1.join()
t2.join()

print_numbers()
print_letters()

finished_time = time.time() - start_time
print(f"Time taken: {finished_time} seconds")