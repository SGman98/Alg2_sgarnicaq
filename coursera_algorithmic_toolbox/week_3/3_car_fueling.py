def solve(distance, max_travel, stops: list):
    current_location, stop_count = 0, 0
    while current_location + max_travel < distance:
        # filter stops that are between current location and current location + max_travel not including current location
        possible_stops = [stop for stop in stops if current_location < stop <= current_location + max_travel]
        if not possible_stops: # if no stops are found, return -1
            return -1
        current_location = max(possible_stops) # set current location to the max of the possible stops
        stop_count += 1 # increment stop count
    return stop_count
    
    
if __name__ == '__main__':
    d,m,n = int(input()),int(input()),int(input())
    stop_list = list(map(int, input().split()))
    print(solve(d,m,stop_list))