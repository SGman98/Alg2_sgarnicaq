def knapsack(weight, wn):
    wn.sort(reverse=True)
    n = len(wn)
    # create a matrix of size (w+1)x(n+1)
    matrix = [[0 for _ in range(weight+1)] for _ in range(n+1)]
    for i in range(1, n + 1):
        for j in range(1, weight + 1):
            matrix[i][j] = matrix[i-1][j]
            if wn[i-1] <= j:
                val = matrix[i-1][j-wn[i-1]] + wn[i-1]
                if matrix[i][j] < val:
                    matrix[i][j] = val
    return matrix[n][weight]


def main():
    w, n = map(int, input().split())
    wn = list(map(int, input().split()))
    print(knapsack(w, wn))


if __name__ == "__main__":
    main()
