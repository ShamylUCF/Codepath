def is_balanced(code):
    freq = {}
    freq_of_values = {}

    for x in code:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1

    for value in freq.values():
        if value in freq_of_values:
            freq_of_values[value] += 1
        else:
            freq_of_values[value] = 1
    
    print(freq_of_values)
    
    if len(freq_of_values) == 1:
        return False
    if len(freq_of_values) == 2:
        for x in freq_of_values:
            if freq_of_values[x] == 1:
                return True
        return False 
    if len(freq_of_values) > 2:
        return False


code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 