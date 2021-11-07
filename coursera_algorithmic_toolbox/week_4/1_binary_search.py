def bin_search(list_, i):
    low, high = 0, len(list_) - 1
    while low <= high:
        mid = (low + high) // 2
        if list_[mid] == i:
            return mid
        if list_[mid] < i:
            low = mid + 1
        else:
            high = mid
    return -1

if __name__ == '__main__':
    n = int(input())
    list_ = [int(x) for x in input().split()]
    k = int(input()) 
    search_list = [int(x) for x in input().split()]

    print(' '.join([str(bin_search(list_, i)) for i in search_list]))