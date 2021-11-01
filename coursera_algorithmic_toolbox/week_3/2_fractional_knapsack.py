def solve(item_list, capacity):
    # sort items by value/weight ratio → item[0] is value, item[1] is weight
    item_list = sorted(item_list, key=lambda x: x[0]/x[1], reverse=True)
    value, current_weight = 0, 0
    for item in item_list:
        # if item weight less than capacity, add item to knapsack
        if current_weight + item[1] <= capacity:
            value += item[0]
            current_weight += item[1]
        # if item weight more than capacity, add fraction of item to knapsack
        else:
            value += item[0] * (capacity - current_weight) / item[1]
            break
    print("{:.4f}".format(value))

if __name__ == '__main__':
    n, w = map(int, input().split())
    value_weight = [list(map(int, input().split())) for _ in range(n)]
    solve(value_weight, w)