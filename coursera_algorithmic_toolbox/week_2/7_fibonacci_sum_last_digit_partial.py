def fibonacci_sum_last_digit_partial(from_, to_):
    a, b, sum = 0, 1, 0
    # pattern of sum fibonacci sequence repeats at 60
    from_ = from_ % 60
    to_ = to_ % 60
    # makes sure that to_ is greater than from_
    if from_ > to_:
        to_ += 60

    for i in range(to_):
        a, b = b, (a + b) % 10
        if i >= from_ - 1:
            sum = (sum + a) % 10
    return sum

if __name__ == '__main__':
    from_, to_ = map(int, input().split())
    print(fibonacci_sum_last_digit_partial(from_, to_))