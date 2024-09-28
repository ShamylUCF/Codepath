def is_authentic_collection(art_pieces):

    if len(art_pieces) <= max(art_pieces):
        return False
    
    n = len(art_pieces) - 1
    freq = {}
    arr = []

    for x in art_pieces:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1

    for key in freq.keys():
        arr.append(key)
    arr.sort()

    for i in arr:
        if i == n:
            return freq[i] == 2
        else:
            return freq[i] == 1

collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))