def primitive_calc(n):
    # Table [i, j] where
    # i is number of operations needed to get to index
    # j is the reference of the number it cames from
    table = [[0,0]] * (n+1) # Matrix of size n+1 x 2

    def min_ref(val):
        if val == int(val) and table[int(val)][0] < min:
            return table[int(val)][0], int(val)

    for index in range(2, n + 1):
        min, ref = float('inf'), 1
        min, ref = min_ref(index / 2) or (min, ref)
        min, ref = min_ref(index / 3) or (min, ref)
        min, ref = min_ref(index - 1) or (min, ref)
        table[index] = [min + 1, ref]

    print(table[n][0])

    steps, index = [n], n
    while (index := table[index][1]) != 0:
        steps.append(index)
    print(' '.join(str(i) for i in reversed(steps)))

def main():
    n = int(input())
    primitive_calc(n)

if __name__ == '__main__':
    main()
