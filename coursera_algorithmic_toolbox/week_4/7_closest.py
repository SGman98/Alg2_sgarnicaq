import math

def brute_force(points):
    min_distance = 10000
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            new_distance = distance(points[i], points[j])
            if new_distance < min_distance:
                min_distance = new_distance
    return min_distance

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def divide(points):
    points = sorted(points, key=lambda x: x[0])
    half = len(points) // 2
    middle_line = (points[half - 1][0] + points[half][0]) / 2
    min_distance_div = min(brute_force(points[:half]), brute_force(points[half:]))
    trim = list(filter(lambda x: abs(middle_line - x[0]) < min_distance_div, points))
    trim = sorted(trim, key=lambda x: x[1])
    result = min([brute_force(trim[i:i+7]) for i in range(len(trim)-1)]) if trim else min_distance_div

    # print(f'{points = }')
    # print(f'{half = }')
    # print(f'{points[:half] = } --- {points[half:] = }')
    # print(f'{middle_line = } --- {min_distance_div = }')
    # print(f'{trim = }')
    # print(f'{result = :.6f}')
    return f'{result:.6f}'


if __name__ == '__main__':
    n = int(input())
    points = [tuple(int(x) for x in input().split()) for _ in range(n)]
    print(divide(points))