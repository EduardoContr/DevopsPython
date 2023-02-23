import multiprocessing

import time

y = time.perf_counter()

a = [1,3,2,5,3,8,4,10]
a2 = [32,34,33,34,35,36]

##work to get the average of both lists or min value or index value since using lists we have to be watchful and
##for this example we need to work in a list
def listfx():
    print ('sleeping count turned on and set for 12 seconds')
    time.sleep(12)
    for x in a:
        #modulus example in a for in loop
        if x %2 == 0:
            print (x)
            ##use an f string literal to add some text
            print (f'is even, yes {x} is even')
        else:
            print(x)
            print (f' the number {x} is odd')
    print ('\nthis program just ran succesfully; it was a function call after sleep cycle')

def listfx2():
    print ('sleeping count turned on and set for 14 seconds')
    time.sleep(14)
    for x in a2:
        #modulus example in a for in loop
        if x %2 == 0:
            print (x)
            ##use an f string literal to add some text
            print (f'is even, yes {x} is even')
        else:
            print(x)
            print (f' the number {x} is odd')
    print ('\nthis program just ran succesfully; it was a function call after sleep cycle')



##listfx()

p1 = multiprocessing.Process(target=listfx())
p1.start()
##listfx2()

y2 = time.perf_counter()

print(f'this took a few moments; it took {round(y2-y, 2)} seconds')