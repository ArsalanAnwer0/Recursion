# Sum of Array Elements
# [1,2,3,4,5]
# total -> loop -> 1st element -> last element -> add value to total -> return total

def sum_iterative(arr):
    total = 0
    for num in arr:
        total += num
    return total


def sum_recursive(arr):

    # base case
    if not arr:
        return 0
    
    return arr[0] + sum_recursive(arr[1:])

# hello olleh 

