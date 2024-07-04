import csv
student_file = 'students.csv'
table = []

with open(student_file, 'r', newline = '') as file:
    #student_record = csv.DictReader(file)
    student_record = csv.reader(file)
    #print(student_record)
    count = 0
    for line in student_record:
        if count > 2:
            table.append(line)
        count += 1
    print(table)
    
            
        
        
  
    #table.pop(0)
    #print(table)
    #table.pop(0)
    #print(table)
    
    #print(type(student_record))
    # #print(student_record)
    # for lines in student_record:
    #     print(f"{lines['name']}'s grade is {lines['grade']}")