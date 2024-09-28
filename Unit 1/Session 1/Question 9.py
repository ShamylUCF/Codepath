def get_odds(nums):
    odds = []
    for number in nums:
        if number % 2 == 1:
            odds.append(number)
    return odds

nums = [1, 2, 3, 4]
print(get_odds(nums))

nums = [2, 4, 6, 8]
print(get_odds(nums))
