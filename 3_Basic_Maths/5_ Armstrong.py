def armstrong(n):
    sum = 0
    dup = n
    while n > 0:
        ld = n % 10
        sum = sum + (ld* ld* ld)
        n = n // 10
    
    if sum == dup:
        return True
    else:
        return False
    

N = 55
print(armstrong(N))