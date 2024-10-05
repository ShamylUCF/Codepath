def find_treasure_indices(gold_amounts, target):
    gold_amount_indicies = {}

    for index,value in enumerate(gold_amounts):
        temp = target - value
        if temp in gold_amount_indicies:
            return [gold_amount_indicies[temp], index]
        gold_amount_indicies[value] = index
    
    return []


gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))  
print(find_treasure_indices(gold_amounts2, target2))  
print(find_treasure_indices(gold_amounts3, target3))  