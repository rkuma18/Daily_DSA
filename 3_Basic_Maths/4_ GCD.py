N1 = 20
N2 = 40

def gcd(n1, n2):
    while n1 > 0 and n2 > 0:
        if n1 > n2:
            n1 = n1 % n2
        else:
            n2 = n2 % n1
    return n1 + n2   # one of them will be zero; the other is the GCD

print(gcd(N1, N2))
