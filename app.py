def digit_sum(n):
    s = str(n)
    l = list(map(int,s.strip()))
    return sum(l)

def digital_root(n):
    if n < 10:
        return n
    return digital_root(digit_sum(n))
