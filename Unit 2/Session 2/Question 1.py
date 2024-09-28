def find_balanced_subsequence(art_pieces):
    freq = {}
    arr = []
    max_sum = 0

    for x in art_pieces:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1

    for key in freq.keys():
        arr.append(key)
    arr.sort()
    
    for i in range(len(arr) - 1):
        if arr[i+1] - arr[i] == 1:
            temp = freq[arr[i]] + freq[arr[i+1]]
            if temp > max_sum:
                max_sum = temp
    
    return max_sum
            
        








art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))