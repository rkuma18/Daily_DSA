N = 5

# without recursion
def sum_nat(N):
    total = 0
    for i in range(1, N+1):
        total += i
    print(total)

#sum_nat(5)


def sum_nat_r(n):
    if n == 0:
        return 0
    return n + sum_nat_r(n - 1)

print(sum_nat_r(N))
