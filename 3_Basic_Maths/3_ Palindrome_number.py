def palindrome(n):
    num = 0
    dup = n
    while n > 0:
        ld = n % 10
        num = (num * 10) + ld
        n = n //10

    if num == dup:
        return True
    else:
        return False

N = 77
print(palindrome(N))