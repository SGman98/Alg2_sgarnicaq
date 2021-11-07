def majority_element(list_):
    for i in range(len(list_)):
        current = list_[i]
        count = 0
        for j in range(len(list_)):
            if list_[j] == current:
                count += 1
        if count > len(list_) / 2:
            return 1
    return 0

if __name__ == '__main__':
    n = int(input())
    list_ = [int(x) for x in input().split()]

    print(majority_element(list_))
    # print(int(any(list_.count(i) > n / 2 for i in list_)))