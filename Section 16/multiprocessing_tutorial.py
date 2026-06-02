import multiprocessing

import time

def square_num():
    for i in range(5):
        time.sleep(2)
        print("Square:",i*i)

def cube_num():
    for j in range(5):
        time.sleep(2)
        print("Cube:",j*j*j)

if __name__ == "__main__":

    ## Creating 2 process
    p1 = multiprocessing.Process(target=square_num)
    p2 = multiprocessing.Process(target=cube_num)
    t=time.time()

    ## Start the process
    p1.start()
    p2.start()

    ## Wait for the process to complete
    p1.join()
    p2.join()

    finished_time = time.time()-t
    print(finished_time)