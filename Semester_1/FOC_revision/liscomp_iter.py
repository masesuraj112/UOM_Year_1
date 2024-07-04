# words = ['pencil', 'highlighter', 'paper-clip', 'ruler', 'pen']
# print({char for word in words for char in word })
# #print([{word : len(word)} for word in words])
# iterable = "ABC"
# my_iter = iter(iterable)
# # first = next(my_iter)
# # second = next(my_iter)
# # print(f'{first} is first')
# # print(f'{second} is second')
from itertools import combinations, permutations, product, 
#for combination in combinations('ABC', 2):
    #print(combination)
    
# think of combination like set, they won't print BC and CB only BC
    
# for combination in permutations('ABC', 2):
#     print(combination)

# animals = ['cats', 'dogs', 'hamsters', 'elephants']
# places = ['Melbourne', 'space', 'the supermarket']

# for animal, place in product(animals, places):
#     print(animal, place)
student_scores = [
    ("Alice", 85),
    ("Bob", 90),
    ("Alice", 88),
    ("Bob", 92),
    ("Alice", 91),
    ("Bob", 85),
    ("Alice", 87),
    ("Bob", 89)]
sorted(student_scores, key = lambda x: x[0])
grouped_scores = groupby
"""
for groupby
first sort the list into desired order
declare a variable with grouby(iterator, key = lambda)
"""
