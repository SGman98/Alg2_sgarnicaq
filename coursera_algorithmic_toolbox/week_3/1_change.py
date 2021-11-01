def solve(value):
    # All 10 coin possible then all 5 coin and lastly all 1 coin
    print(value // 10 + value % 10 // 5 + value % 10 % 5)

if __name__ == '__main__':
    solve(int(input()))