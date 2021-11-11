def majority_element(list_):
    list_ = sorted(list_)
    half = len(list_) // 2 # Neccessary number to be majority - 1 (for indexing)
    half_ceil = -(len(list_) // -2) # difference if n is odd or even
    for i in range(half_ceil):
        if list_[i] == list_[i + half]: # If the ith element is equal to the number at maj distance it means it es majority
            return 1
    return 0


if __name__ == '__main__':
    n = int(input())
    list_ = [int(x) for x in input().split()]

    print(majority_element(list_))
    # print(int(any(list_.count(i) > n / 2 for i in set(list_))))