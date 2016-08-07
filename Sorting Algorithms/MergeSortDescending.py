'''
  simple merge sort implementation, descending
'''

def mergeSortDescending(array):

    if(len(array)) <= 1:
        return array

    split = len(array)//2

    left = mergeSortDescending(array[split:])
    right = mergeSortDescending(array[:split])

    return merge(left, right)

def merge(left, right):

    if len(left) is 0:
        return right

    elif len(right) is 0:
        return left
    
    elif left[0] > right[0]:
        return [left[0]] + merge(left[1:], right)
    else:
        return [right[0]] + merge(right[1:], left)


unsorted_array = [10, 5, 7, 23, 1 , 2345, 76 , -1, 8]
sorted_array = mergeSortDescending(unsorted_array)

print(str(sorted_array))
