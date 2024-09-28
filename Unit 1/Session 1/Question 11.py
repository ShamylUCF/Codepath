def running_sum(superhero_stats):
    running_sum = 0
    lst = []
    for crime_stopped in superhero_stats:
        running_sum += crime_stopped
        lst.append(running_sum)
    return lst

superhero_stats = [1, 2, 3, 4]
print(running_sum(superhero_stats))

superhero_stats = [1, 1, 1, 1, 1]
print(running_sum(superhero_stats))

superhero_stats = [3, 1, 2, 10, 1]
print(running_sum(superhero_stats))