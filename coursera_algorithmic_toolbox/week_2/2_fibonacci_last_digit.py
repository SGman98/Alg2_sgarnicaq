def fibonacci_last_digit(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % 10
    return a

if __name__ == '__main__':
    print(fibonacci_last_digit(int(input()))) 