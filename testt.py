import sys
from turtle import *
n=int(sys.argv[1])
size = int(sys.argv[2])
angle = 3
def triangle(size,n):
    for i in range(3):
        fd(size)
        lt(360/n)
        fd(size)
        lt(360/n)
        fd(size)
        rt(180-(720/n))
    lt(60)
print(triangle(size, n))
#def pi(n)






done()