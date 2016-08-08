'''
simple implementation of quicksort - descending
Memory complexity - On the order of O(1) 
Time complexity - Best case: O(nlog(n)), Worst case: O(n^2)
'''
def switch(array, a, b):
    save = array[a]
    array[a] = array[b]
    array[b] = save


def split(array, lower, upper):
    pivot = array[lower]
    while lower <= upper: 
        while array[lower] > pivot:
            lower = lower + 1
        while array[upper] <  pivot:
            upper = upper - 1
        if upper >= lower:
            switch(array, upper, lower) 
            lower = lower + 1 
            upper = upper - 1 
    return lower 
    
def QuickSortDescending(array, lower, upper):
    pivot = split(array, lower, upper)
    
    if lower < (pivot - 1):
        QuickSortDescending(array, lower, pivot - 1)
        
    if upper > pivot:
        QuickSortDescending(array, pivot, upper)

    return array 
    
        
    

#testing
unsorted_array = [10, 5, 7, 23, 1 , 2345, 76 , -1, 8]
sorted_array = QuickSortDescending(unsorted_array, 0, ( len(unsorted_array) - 1 ))

print(str(sorted_array))
