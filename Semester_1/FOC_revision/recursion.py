def sum_list(my_list):
    print(len(my_list))
    if len(my_list) == 0:
        return 0
    
    return my_list[0] + sum_list(my_list[1:])


        
#print(sum_list([1, 2, 3]))

def create_factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    
    return num * create_factorial(num - 1)
    

# print(create_factorial(4))

def power_set (lst): # lists easier than sets
    # head recursion
    if lst == []:
        return [[]]
    rest = power_set(lst[1:])
    print(f'list is {lst}')
    print(f'list[1:] is {lst[1:]}')
    print(f'rest is {rest}')
    result = []
    for item in rest:
        print(f'item is {item}')
        result.append(item)
        result.append([lst[0]] + item)
    return result
#print(power_set(['a', 'b', 'c']))

#Consider an array arr[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91}, and the target = 23.

def find_target(my_arr, target):
    my_list = list(my_arr)
    if len(my_list) == 0:
        return None 
    elif len(my_list) == 1:
        return my_list[0]
    else:
        midpoint = len(my_list) // 2

def recursive_binary_search(arr, target, low, high):
    # Base case: if low is greater than high, the target is not present in the array
    if low > high:
        return -1
    
    # Find the middle index
    mid = (low + high) // 2
    
    # Check if the target is present at the mid index
    if arr[mid] == target:
        return mid
    # If the target is smaller than the mid element, it can only be in the left subarray
    elif arr[mid] > target:
        return recursive_binary_search(arr, target, low, mid - 1)
    # Otherwise, the target can only be in the right subarray
    else:
        return recursive_binary_search(arr, target, mid + 1, high)
    
    