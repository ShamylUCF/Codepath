def most_honey(height):
    left_pointer = 0
    right_pointer = len(height) - 1
    max_area = 0

    while left_pointer < right_pointer:

        width = right_pointer - left_pointer
        area = min(height[left_pointer],height[right_pointer]) * width

        if area > max_area:
            max_area = area

        if height[left_pointer] < height[right_pointer]:
            left_pointer += 1
        else:
            right_pointer -= 1
    
    return max_area



height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(most_honey(height))

# height2 = [1,2,1]
# print(most_honey(height2))
