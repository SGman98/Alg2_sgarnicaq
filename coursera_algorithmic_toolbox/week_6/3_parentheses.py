# split string into array of values and operators
def split_string(s):
    values = []
    operators = []
    for i in range(len(s)):
        if s[i] in ['+', '-', '*']:
            operators.append(s[i])
        else:
            values.append(int(s[i]))
    return values, operators


# Calculate the max and min values for a given operator
def min_max(i,j,matrix_min,matrix_max, operators):
    min_val = float('inf')
    max_val = float('-inf')
    for k in range(i,j):
        a = eval( str(matrix_max[i][k]) + operators[k] + str(matrix_max[k+1][j]) )
        b = eval( str(matrix_max[i][k]) + operators[k] + str(matrix_min[k+1][j]) )
        c = eval( str(matrix_min[i][k]) + operators[k] + str(matrix_max[k+1][j]) )
        d = eval( str(matrix_min[i][k]) + operators[k] + str(matrix_min[k+1][j]) )
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)
    return min_val, max_val


def parentheses(s):
    values, operators = split_string(s)

    # create a matrix of len(value)
    matrix_min = [[0 for _ in range(len(values))] for _ in range(len(values))]
    matrix_max = [[0 for _ in range(len(values))] for _ in range(len(values))]

    # initialize the diagonal with the values
    for i in range(len(values)):
        matrix_min[i][i] = values[i]
        matrix_max[i][i] = values[i]

    for s in range(1, len(values)):
        for i in range(len(values)-s):
            j = i + s
            matrix_min[i][j], matrix_max[i][j] = min_max(i,j,matrix_min,matrix_max, operators)

    return matrix_max[0][len(values)-1]


def main():
    string_input = input()
    print(parentheses(string_input))


if __name__ == "__main__":
    main()