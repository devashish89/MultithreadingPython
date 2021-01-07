import time
import threading
lst_squares = []
lst_cubes = []

def square_nums(numbers):
    global lst_squares
    numbers = list(numbers)
    #print(list(map(lambda x:x*x,numbers)))
    for num in numbers:
        time.sleep(0.2)
        print(f"Square of {num} is {num*num}")
        lst_squares.append(num*num)

def cube_nums(numbers):
    numbers = list(numbers)
    #print(list(map(lambda x:x*x*x,numbers)))
    for num in numbers:
        time.sleep(0.2)
        print(f"Cube of {num} is {num*num*num}")
        lst_cubes.append(num*num*num)

print(__name__)
if __name__=='__main__':
    lst = [1,2,3,4]


    thread1 = threading.Thread(target=square_nums, args=(lst,))
    thread2 = threading.Thread(target=cube_nums, args=(lst,))

    t1 = time.time()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Done!!")

    t2 = time.time()
    print("Time taken",t2-t1)

    print(lst_squares, lst_cubes) #threads are lightweigiht and use shared memory