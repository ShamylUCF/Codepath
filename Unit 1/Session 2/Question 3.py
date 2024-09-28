def remove_dupes(items):
    low_pointer = 0
    high_pointer = 1

    while high_pointer < len(items):
        if items[low_pointer] == items[high_pointer]:
            items.remove(items[low_pointer])
        low_pointer += 1
        high_pointer += 1

    return len(items)

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
print(remove_dupes(items))

items2 = ["extract of malt", "haycorns", "honey", "thistle"]
print(remove_dupes(items2))

