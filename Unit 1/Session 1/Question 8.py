def find_villain(things, villain):
    '''Function to find the villian in a crowd'''
    indexes = []
    for index, things in enumerate(crowd):
        if things == villain:
            indexes.append(index)
    return indexes


crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
VILLIAN = 'The Joker'

print(find_villain(crowd, VILLIAN))
