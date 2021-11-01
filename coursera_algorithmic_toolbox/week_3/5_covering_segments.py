def solve(coor):
    coor = sorted(coor) # sort by start point of segments
    points = []
    while len(coor) > 0:
        # if the segments don't overlap or if it is the last segment/intersection
        if len(coor) == 1 or coor[0][1] < coor[1][0]:
            points.append(coor[0][1])
        else: # if the first segment overlaps the next one
            coor[1][1] = min(coor[0][1], coor[1][1]) # then intersect them
        coor.pop(0)
    print(len(points))
    print(*points)
    return
      
if __name__ == "__main__":
    n = int(input())
    coor = [list(map(int,input().split())) for _ in range(n)]
    solve(coor)
        