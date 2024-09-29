def organize_pirate_crew(group_sizes):
    dic = {}
    for pirate,group in enumerate(group_sizes):
        if group in dic:
            dic[group].append(pirate)
        else:
            dic[group] = []
            dic[group].append(pirate)
        
    result = []

    for key,value in dic.items():
        for i in range(0, len(value), key):
            result.append(value[i:i + key])

    return result


group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
group_sizes2 = [2, 1, 3, 3, 3, 2]

print(organize_pirate_crew(group_sizes1))
print(organize_pirate_crew(group_sizes2)) 