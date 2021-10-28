def fibonacci_sum_square_last_digit(n):
    a, b= 0, 1
    for _ in range(n % 60):
        a, b = b, (a+ b) % 10
    return (a * b) % 10

if __name__ == '__main__':
    print(fibonacci_sum_square_last_digit(int(input())))