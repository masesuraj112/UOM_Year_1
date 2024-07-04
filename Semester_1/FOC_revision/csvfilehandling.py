import csv
from collections import defaultdict
def count_sales(csv_filename):
    #my_dict = {}
    my_dict = defaultdict(int)
    # opens the file 
    with open(csv_filename) as file:
        # converts the file to DictReader
        myfile = csv.DictReader(file)
        
        # Iterates through dictionary
        for line in myfile:
            my_dict[line['Product']] += 1
            # #print(f'line is {line}')
            # # Checks if specific Product exists in my_dict
            # if line['Product'] in my_dict.keys():
            #     my_dict[line['Product']] += 1
            # else:
            #     # If it doesn't exist adds into my_dict -> magic
            #     my_dict[line['Product']] = 1
        return dict(my_dict)
print(count_sales('dog.csv'))
# This is hardcoding 