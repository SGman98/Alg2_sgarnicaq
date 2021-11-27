def lcs3(a, b, c):
    n = len(a)
    m = len(b)
    l = len(c)
    matrix3 = [[[0] * (l + 1) for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]: # if value matches
                    matrix3[i][j][k] = matrix3[i - 1][j - 1][k - 1] + 1 # add 1 to the diagonal
                else:
                    # if not, take the max of the three adjacent values 
                    matrix3[i][j][k] = max(matrix3[i - 1][j][k], matrix3[i][j - 1][k], matrix3[i][j][k - 1])

    return matrix3[n][m][l]

def main():
    _ = input()
    a = list(map(int, input().split()))
    _ = input()
    b = list(map(int, input().split()))
    _ = input()
    c = list(map(int, input().split())) 
    print(lcs3(a, b, c))

if __name__ == '__main__':
    main()
