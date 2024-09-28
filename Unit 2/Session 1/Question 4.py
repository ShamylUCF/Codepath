def is_balanced(code):
    code_dictionary = {}
    totals = {}
    finding_val = 0

    for x in code:
        if x in code_dictionary:
            code_dictionary[x] += 1
        else:
            code_dictionary[x] = 1

    for key,value in code_dictionary.items():
        if value in totals:
            totals[value] += 1
        else:
            totals[value] = 1
    
    print(totals)

    if len(totals) != 2:
        return False
    
    if totals.keys() > totals[1] and  totals[0] - 1 == totals[1]:
        return True
    
    if (totals[1] > totals[0]) and  (totals[1] - 1 == totals[0]):
        return True
    
    return False


code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 