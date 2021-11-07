def majority_element(list_):
    list_ = sorted(list_)
    maj = len(list_) // 2
    for i in range(maj + 1):
        if list_[i] == list_[i + maj]:
            return 1
    return 0


if __name__ == '__main__':
    n = int(input())
    list_ = [int(x) for x in input().split()]

    print(majority_element(list_))
    # print(int(any(list_.count(i) > n / 2 for i in set(list_))))