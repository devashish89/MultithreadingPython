import time

def square_nums(numbers):
    numbers = list(numbers)
    #print(list(map(lambda x:x*x,numbers)))
    for num in numbers:
        time.sleep(0.2)
        print(num*num)

def cube_nums(numbers):
    numbers = list(numbers)
    #print(list(map(lambda x:x*x*x,numbers)))
    for num in numbers:
        time.sleep(0.2)
        print(num*num*num)

print(__name__)
if __name__=='__main__':
    lst = [1,2,3,4]
    t1 = time.time()
    square_nums(lst)
    cube_nums(lst)
    t2 = time.time()
    print("Time taken",t2-t1)

