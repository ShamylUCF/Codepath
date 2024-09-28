def shuffle(cards):
    low = 0
    mid = int(len(cards)/2)

    shuffled_deck = []

    while mid != len(cards):
        shuffled_deck.append(cards[low])
        shuffled_deck.append(cards[mid])
        low += 1
        mid += 1
    return shuffled_deck

cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
print(shuffle(cards))

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
print(shuffle(cards))

cards = [10, 10, 2, 2]
print(shuffle(cards))
