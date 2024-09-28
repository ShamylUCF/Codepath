def find_duplicate_chests(chests):

    chest_dictionary  = {}
    duplicates= []

    for x in chests:
        if x in chest_dictionary:
            chest_dictionary[x] += 1
        else:
            chest_dictionary[x] = 1
    print(chest_dictionary)

    for key, value in chest_dictionary.items():
        if value == 2:
            duplicates.append(key)
    return duplicates

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))