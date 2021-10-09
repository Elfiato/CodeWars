def sum_of_intervals(intervals):
    full_line = []
    for interval in intervals:
        full_line.extend(range(interval[0], interval[1]+1))
    return len(set(full_line))

print(sum_of_intervals([[1, 4], [7, 10], [3, 5]]))