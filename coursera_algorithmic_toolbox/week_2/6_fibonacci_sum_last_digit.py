def fibonacci_sum_last_digit(n):
    a, b, sum = 0, 1, 0
    # Pattern of sum fibonacci sequence repeats at 60
    for _ in range(n % 60):
        a, b = b, (a + b) % 10
        sum = (sum + a) % 10
    return sum

if __name__ == '__main__':
    print(fibonacci_sum_last_digit(int(input())))