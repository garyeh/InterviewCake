# Merging meeting times
# O(nlogn) time
# O(n) space

def merge_times(times):
    sorted_times = sorted(times)
    merged = [sorted_times[0]]

    for i in range(len(sorted_times)):
        if merged[-1][1] >= sorted_times[i][0]:
            start_time = merged[-1][0]
            end_time = max(sorted_times[i][1], merged[-1][1])
            merged[-1] = (start_time, end_time)
        else:
            merged.append(sorted_times[i])
    return merged

print merge_times([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
print merge_times([(1, 5), (2, 3)])
print merge_times([(1, 10), (2, 6), (3, 5), (7, 9)])
