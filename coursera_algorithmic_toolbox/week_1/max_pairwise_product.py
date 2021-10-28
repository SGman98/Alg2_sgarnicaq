def max_pairwise_product(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2]

if __name__ == '__main__':
    if int(input()) < 2:
        print(0)
    numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(numbers))