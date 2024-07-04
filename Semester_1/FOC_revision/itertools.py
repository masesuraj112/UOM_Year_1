# for element in [1 , 2 , 3]:
#     print (element)
    
# count = 1
# while count < 4:
#     print(count)
#     count +=1
    
# count = 0
# table = [1, 2, 3, 5]
# while count < len(table):
#     print(table[count])
#     count += 1
from itertools import product, cycle
def get_deck ():
    suits = 'CDHS'
    values = '234567890JQKA'
    name = 'ABCD'
    deck = product (values , suits)
    deck_1 = product (values , suits)
    for d in deck:
        #print(d)
        return ([''. join (c) for c in deck_1])
#print(get_deck())
def deal ():
    """ Put cards in 4 equal piles . """
    deck = get_deck ()
    hands = [[] , [] , [] , []]
    players = cycle(hands)
    for card in deck :
        player = next ( players )
        player.append(card)
        return ( hands )
print(deal()[0])
print(deal()[1])
print(deal()[2])
print(deal()[3])


