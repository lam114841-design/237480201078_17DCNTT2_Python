def so_chan(n):
    return n % 2 == 0

def so_hoan_hao(n):
    if n <= 0:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def so_chinh_phuong(n):
    return int(n**0.5)**2 == n

def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def bcnn(a, b):
    return abs(a*b) // ucln(a, b)

def nguyen_to_cung_nhau(a, b):
    return ucln(a, b) == 1