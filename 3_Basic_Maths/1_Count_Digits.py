def count_digit(number):
    ls = list(str(number))
    total_len = len(ls)
    return total_len
    

def cnt_digit(n):
    cnt = 0
    while n > 0:
        cnt += 1
        n = n // 10
    return cnt


N = 7789
print(count_digit(N))
print(cnt_digit(N))