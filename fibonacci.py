
def fib(num):
    assert num>=0 and int(num)==num
    if num==0:
        return 0
    if num==1:
        return 1
    return fib(num-1)+ fib(num-2)





print(fib(10))