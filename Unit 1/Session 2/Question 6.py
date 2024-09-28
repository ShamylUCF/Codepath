def merge_intervals(intervals):
    left_pointer = 0
    right_pointer = 1

    intervals.sort()

    while(right_pointer < len(intervals)):

        if intervals[right_pointer][0] >= intervals[left_pointer][0] and intervals[right_pointer][0] <= intervals[left_pointer][1]:
            if intervals[left_pointer][1] > intervals[right_pointer][1]:
                intervals.pop(right_pointer)
            else:
                intervals[left_pointer][1] = intervals[right_pointer][1]
                intervals.pop(right_pointer)
        elif intervals[right_pointer] == intervals[left_pointer]:
            intervals.pop(right_pointer)
        else:
            left_pointer +=1 
            right_pointer +=1 
        
    return intervals


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))

intervals2 = [[1,4],[2,3]]
print(merge_intervals(intervals2))
