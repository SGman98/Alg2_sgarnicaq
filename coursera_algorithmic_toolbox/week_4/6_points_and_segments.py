def points_and_segments(segments, points):
    # For each point count in how many segments it exists
    return [len(list(filter(lambda x: x[0] <= point and x[1] >= point, segments))) for point in points]


if __name__ == '__main__':
    s, p = map(int,input().split())
    segments = [[int(x) for x in input().split()] for _ in range(s)]
    points = [int(x) for x in input().split()]
    print(*points_and_segments(segments, points), sep=' ')