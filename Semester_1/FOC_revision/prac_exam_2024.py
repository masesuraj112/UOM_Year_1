# def split_any(text, delims):
#     result = []
#     curr = ""
    
#     for char in text:
#         if char not in delims:
#             curr += char
#             print(f"{curr} is curr")
#         elif len(curr.strip(" ")) == 1:
#             print(f'{result} is result')
#             # .strip() removes leading whitespace 
#             result.append(curr.strip())
#             curr = ""
#     print(result)
#     print(f'{curr} is curr')
#     print(result[0].strip())
    
#     # checks final trailing one 
#     if result[-1].strip() != " ":
#         result.append(curr.strip())
        
#     return result 
# #print(split_any("a,b,c", ","))
# #print(split_any("1+8-3=6", "-+="))
# print(split_any(" 1+8 -3=6  ", "-+="))


# ""
# "a"
# "a".strip()
# "ab"
# ["ab"]

# How to save file
# Open file, loop through the zbinis, write, close 
zbinis = ['bruh', 'bruh1', 'blah,']
def save_zbinis(zbinis, filename):
    with open(filename, 'a') as file:
        for z in zbinis:
            file.write(z)
save_zbinis(zbinis, filename='something.txt')
