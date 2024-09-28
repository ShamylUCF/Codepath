def sort_by_parity(nums):
    evens = []
    odds = []

    for num in nums:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    
    evens.extend(odds)
    return evens

nums = [3, 1, 2, 4]
print(sort_by_parity(nums))

nums2 = [0]
print(sort_by_parity(nums2))