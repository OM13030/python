#fibonacci series
# 0 1 1 2 3 5 8 13
'''
fib(0) = 0
fib(1) = 1
fib(2) = fib(0) + fib (1)
fib(3) = fib(1) + fib(2)
fin(n) = fib(n-2) + fib(n-1)

'''

def fibonacci(n):
    # base case
    if(n == 0 or n == 1 ):
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))