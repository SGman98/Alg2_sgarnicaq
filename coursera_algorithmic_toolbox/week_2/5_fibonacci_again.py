def fibonacci(n, m):
    a, b = 0, 1
    for _ in range(n % pisano_period(m)):
        a, b = b, (a + b) % m
    return a

def pisano_period(m):
    a, b = 0, 1
    for i in range(m ** 2):
        a, b = b, (a + b) % m
        if a == 0 and b == 1:
            return i + 1

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(fibonacci(a,b))