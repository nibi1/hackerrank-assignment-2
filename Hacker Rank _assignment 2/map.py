cube = (lambda x : x**3)
fib = []
def fibonacci(n):
    # return a list of fibonacci numbers
    for i in range(0, n):
        if i == 0:
            x = 0
            fib.append(x)
        if i == 1:
            x = 1
            fib.append(x)
        if i > 1:
            x = (fib[i-1]+fib[i-2])
            fib.append(x)
    return fib

