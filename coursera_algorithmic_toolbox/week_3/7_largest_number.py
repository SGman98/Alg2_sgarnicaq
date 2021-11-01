def solve(list_): # O(n*log(n))
    # calculate the result number of digits
    result_len = sum(len(str(x)) for x in list_) # O(n)
    # sort the list by the number extended to the same length of result. if result lenght is 5, and num is 15 then the num will be extended to 15151
    result = sorted(list_,key=lambda item: int((str(item)*-(-result_len//len(str(item))))[:result_len]),reverse=True) # O(n*log(n))
    print(''.join(str(x) for x in result))
    
if __name__ == '__main__':
    n = int(input())
    list_ = [int(x) for x in input().split()]
    solve(list_)