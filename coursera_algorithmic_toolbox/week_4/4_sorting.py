def partition_3(list_, low, high):
    pivot = list_[low]
    j = low + 1 # j is used to compare values
    while j <= high:
        if list_[j] < pivot: # if the value in j is less than the pivot
            list_[low], list_[j] = list_[j], list_[low] # swap with low
            low += 1
            j += 1
        elif list_[j] > pivot: # if the value in j is greater than the pivot
            list_[j], list_[high] = list_[high], list_[j] # swap with high
            high -= 1
        else: # if the value is equal just ignore
            j += 1
    return low, high # low is the index of the first appearance of pivot, and j-1 is the index of the last appearance of pivot

def quick_sort(list_, low, high): # tail recursion elimination
    while low < high:
        mid1, mid2 = partition_3(list_, low, high)
        if mid1 - low < high - mid2:
            quick_sort(list_, low, mid1 - 1)
            low = mid2 + 1
        else:
            quick_sort(list_, mid2 + 1, high)
            high = mid1 - 1
    return list_

if __name__ == '__main__':
    n = int(input())
    list_ = [int(x) for x in input().split()]
    print(' '.join([str(x) for x in quick_sort(list_, 0, len(list_) - 1)]))