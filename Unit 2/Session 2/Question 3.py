def organize_exhibition(collection):
    freq = {}
    matrix = []

    for x in collection:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1

    matrix_rows = max(freq.values())

    for x in range(matrix_rows):
        row = []
        for key in freq.keys():
            row.append(key)
            freq[key] -= 1
            if freq[key] == 0:
                freq.pop(key)
        matrix.append(row)

    return matrix
            
            








collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
              "Kahlo", "O'Keefe"]
collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

print(organize_exhibition(collection1))
print(organize_exhibition(collection2))