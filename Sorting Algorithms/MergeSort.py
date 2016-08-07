'''
 simple merge sort implementation, ascending
'''
def mergeSort(array):
    
    if len(array) <= 1:
        return array

    split = len(array) // 2

    left = mergeSort(array[split:])
    right = mergeSort(array[:split])
    
    return merge(left, right) 
 

def merge(left, right):

    if len(left) is 0:
        return right
    elif len(right) is 0:
        return left
    elif left[0] <= right[0]:
         return [left[0]]  + merge(left[1:], right)
    else:
        return [right[0]] + merge (right[1:], left) 
        

#testing       
unsorted_array = [10, 5, 7, 23, 1 , 2345, 76 , -1, 8]
sorted_array = mergeSort(unsorted_array)

print(str(sorted_array))
