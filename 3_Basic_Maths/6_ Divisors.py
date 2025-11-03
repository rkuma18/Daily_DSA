import math
def divisor(num):
    res = []
    for i in range(1, int(math.isqrt(num)) + 1):
        if num % i == 0:
            res.append(i)
            if i != num // i:
                res.append(num // i)
    return res

N = 36
print(divisor(N))