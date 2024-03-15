#Testing the speed of two different approaches to count how many leap year
# The first method is mine which took approx 50 % of the second method 
# The second method is from uni slides 

import time 
boolean_count = 0
start_time = time.time()
for year in range(1, 1000000000):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        continue
    else:
        boolean_count +=1
       
end_time = time.time()
print(f'It took {end_time - start_time} seconds using Method 1')
print(f'There were {boolean_count} leap years in the range using Method 2') 
        
start_time_1 = time.time()
boolean_count_1 = 0
for year in range(1, 1000000000):
    
    if year % 400 == 0: 
        
        boolean_count_1 +=1
    elif year % 100 == 0:
        
        continue
    elif year % 4 == 0:
        
        boolean_count_1 +=1
    else :
        continue
        
end_time_1 = time.time()
print(f'It took {end_time_1 - start_time_1} seconds using Method 2')
print(f'There were {boolean_count_1} leap years in the range using Method 2') 



