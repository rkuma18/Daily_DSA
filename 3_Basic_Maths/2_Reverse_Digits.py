def rev_num(n):
    num = 0
    while n > 0:
        ld = n % 10
        num = (num * 10) + ld
        n = n // 10
    return num

N = 12345
print(rev_num(N))