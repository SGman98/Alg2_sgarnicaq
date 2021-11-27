def lcs2(a, b):
    n = len(a)
    m = len(b)
    matrix = [[0] * (m + 1) for _ in range(n + 1)] # matrix n+1 x m+1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]: # if value matches
                matrix[i][j] = matrix[i - 1][j - 1] + 1 # add 1 to the diagonal
            else:
                # if not, take the max of the two values above and to the left
                matrix[i][j] = max(matrix[i][j - 1], matrix[i - 1][j])

    return matrix[n][m]

def main():
    _ = int(input())
    a = [int(x) for x in input().split()]
    _ = int(input())
    b = [int(y) for y in input().split()]
    print(lcs2(a, b))

if __name__ == '__main__':
    main()
