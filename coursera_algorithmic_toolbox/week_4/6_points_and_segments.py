def points_and_segments(segments, points):
    # For each point count in how many segments it exists
    return [[point in range(segment[0], segment[1]) for segment in segments].count(True) for point in points]


if __name__ == '__main__':
    s, p = map(int,input().split())
    segments = [[int(x) for x in input().split()] for _ in range(s)]
    points = [int(x) for x in input().split()]
    print(*points_and_segments(segments, points), sep=' ')