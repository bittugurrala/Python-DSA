#ThreeSum for printing the values

def threeSum(array):
    
    res = []
    #sort the list
    array.sort()
    
    #creating the starting pointer fixed pointer
    for index, value in enumerate(array):               #index = 0, value = -1
        if index >0 and value == array[index - 1]:      #False
            continue
        
        #creating pointers for the other two numbers
        left = index + 1
        right = len(array)-1
        
        while left < right:
            threeSum = value + array[left] + array[right]
            if threeSum > 0:
                right = right -1
            elif threeSum < 0:
                left = left +1
            else:
                res.append([value, array[left], array[right]])
                left = left + 1
                
            #handling the edge condition for two pointer to not repeat elements   Example = [-2, -2, 0, 0, 2, 2]
                while array[left] == array[left-1] and left < right:
                    left = left + 1
            
    return res
    


array = [-1,0,1,2,-1,-4]
print(threeSum(array))


"""
Sorting: Sorting the array is crucial for the two-pointer technique.
Avoiding Duplicates: Skip duplicates for both the fixed pointer and the two pointers to avoid repeated triplets.
Two-Pointer Technique: Efficiently find pairs that sum to a specific value by adjusting the pointers based on the current sum.
"""

