def solve(n):
    num = []
    for i in range(1,n+1):
        sum_num = (i*(i+1))/2 # calculate the sum of the numbers from 1 to i
        if sum_num < n: # if the sum is less than n continue
            continue
        if sum_num == n: # if the sum is equal to n
            num = [x for x in range(1,i+1)] # return the numbers from 1 to i
        else: # if the sum is greater than n
            num = [x for x in range(1,i)] # return the numbers from 1 to i - 1
            num[-1] += n - int(sum_num - i) # add the difference to the last number
        break
        
    print(len(num))
    print(*num, sep=' ')
        
if __name__ == '__main__':
    n = int(input())
    solve(n)