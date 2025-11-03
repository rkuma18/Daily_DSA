N = 5

def fact(N):
    total = 1
    for i in range(1, N+1):
        total *= i
    print(total)

#fact(N)

def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1

    # Recursive case: n * factorial of (n-1)
    return n * factorial(n - 1)

print(factorial(N))