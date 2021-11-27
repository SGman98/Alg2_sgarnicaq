def edit_distance(string1, string2):
    n = len(string1)
    m = len(string2)
    matrix = [[0] * (m + 1) for _ in range(n + 1)] # matrix n+1 x m+1

    for i in range(n + 1):
        matrix[i][0] = i
    for j in range(m + 1):
        matrix[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            insertion = matrix[i][j - 1] + 1
            deletion = matrix[i - 1][j] + 1
            match = matrix[i - 1][j - 1]
            mismatch = matrix[i - 1][j - 1] + 1

            if string1[i - 1] == string2[j - 1]:
                matrix[i][j] = min(insertion, deletion, match)
            else:
                matrix[i][j] = min(insertion, deletion, mismatch)

    return matrix[n][m]

def main():
    s1 = input()
    s2 = input()
    print(edit_distance(s1, s2))

if __name__ == '__main__':
    main()
