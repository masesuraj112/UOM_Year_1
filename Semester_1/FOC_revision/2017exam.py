#print(sorted({'human': ['arthur', 'trillian'], 'robot': ['marvin']}.values())[1][-1])
#print({'human': ['arthur', 'trillian'], 'robot': ['marvin']}.values())
#print(sorted({'human': ['arthur', 'trillian'], 'robot': ['marvin']}.values()))
# sorted takes out the dict_values and turns it into normal list 

# for i in range(8,10):
#     for j in 'HD':
#         print(str(i) + j)
#[str(i) + j for i in range(8, 10) for j in 'HD']
# [condition, outer, inner]
string = '8-0*9-0'
delimeter = ['*', '-']
for char in delimeter:
    string = ''.join(string.split(char))
print(string)
print(string.split())
print('7-9,9'.split('-'))
print('-'.join(['Y', 'o', 'm']))
