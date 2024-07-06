"""
###########This approch is used only if the array is sorted###############
The Two Pointer approach is commonly used 
to solve problems where you need to find pairs of elements in a sorted array that sum up to a specific target value.
Here, you want to find two numbers in the array that add up to the target value.

Here’s a step-by-step implementation of the Two Pointer approach for your problem:

-> Initialize two pointers: one starting at the beginning (left) and one at the end (right) of the array.
-> Calculate the sum of the elements at these two pointers.
-> If the sum is equal to the target, return the indices (or values) of these elements.
-> If the sum is less than the target, move the left pointer one step to the right.
-> If the sum is greater than the target, move the right pointer one step to the left.
-> Repeat steps 2-5 until the pointers meet.
"""

def TwoPointer(array, Target):
    
    #define Two pointers Left and Right 
    left = 0
    right = len(array)-1
    
    #Iterate over the array 
    while left < right:
        current_sum = array[left]+ array[right]
        
        #create the conditions to move the pointers
        if current_sum == Target:
            return [left, right]
            
        elif current_sum > Target:
            right = right -1    #Move towards left
            
        else:
            left =left+1   #Move towards right 
            
    #Return None if nothing found        
    return None
        
array = [3,2,4]
Target = 6
print(TwoPointer(array, Target))