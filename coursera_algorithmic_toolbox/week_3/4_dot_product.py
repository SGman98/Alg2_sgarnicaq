def dot_product(n, v1, v2):
    # sort the vectors and calculate the dot product
    v1.sort()
    v2.sort()
    print(sum([v1[i] * v2[i] for i in range(n)]))

if __name__ == '__main__':
    n = int(input())
    v1 = [int(i) for i in input().split()]
    v2 = [int(i) for i in input().split()]
    dot_product(n, v1, v2)