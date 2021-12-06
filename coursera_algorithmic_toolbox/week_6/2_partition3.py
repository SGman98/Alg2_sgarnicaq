def can_partition3(nums):
    sum_nums = sum(nums) # sum of all numbers
    if sum_nums % 3 != 0: # if sum is not divisible by 3
        return 0 # return 0
    sum_3 = sum_nums // 3 # sum_3 is the sum of all numbers divided by 3
    matrix = [[0 for _ in range(sum_3 + 1)] for _ in range(len(nums) + 1)]
    matrix[0][0] = 1 # initializing 0,0 to 1 to start adding

    # iterate through all the matrix
    for i in range(1, len(nums) + 1):
        for j in range(sum_3 + 1):
            if j - nums[i - 1] >= 0: # if sum_3 is greater than or equal to the current number
                # matrix[i][j] = the number directly above or the number above and number to the left
                # it means that the sum up to j is possible
                matrix[i][j] = matrix[i - 1][j] or matrix[i - 1][j - nums[i - 1]]
            else:
                # if the sum_3 is less than the current number, then it can't add the numbers together
                # so just carry the number above
                matrix[i][j] = matrix[i - 1][j]
    return matrix[-1][-1] # if the number in -1, -1 is 1, then it means that the number can be partitioned


def main():
    n = int(input())
    nums = [int(i) for i in input().split()]
    print(can_partition3(nums))


if __name__ == '__main__':
    main()
