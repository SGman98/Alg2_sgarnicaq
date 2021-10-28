def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        return (a * b) // gcd(a, b)

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b) 

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lcm(a, b))