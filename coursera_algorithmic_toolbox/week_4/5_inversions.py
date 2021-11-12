def merge_sort(list_):
    n = len(list_)
    if n == 1:
        return list_, 0
    m = n // 2
    b, invb = merge_sort(list_[0:m])
    c, invc = merge_sort(list_[m:n+1])
    a_, inversions = merge(b,c)
    return a_, invb + invc + inversions

def merge(b,c):
    d = []
    inversions = 0
    while b and c:
        if b[0] <= c[0]:
            d.append(b.pop(0))
        else:
            d.append(c.pop(0))
            inversions += 1 * len(b)
    d += b + c
    return d, inversions

if __name__ == '__main__':
    n = int(input())
    list_ = [int(x) for x in input().split()]
    print(merge_sort(list_)[1])