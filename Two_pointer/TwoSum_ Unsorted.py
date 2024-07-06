"""
                                ################ When the given array is not Sorted###############
                                Link : https://youtu.be/luicuNOBTAI

The logic behind the hash map (dictionary) approach for finding two numbers in an array that add up to a target value can be understood step-by-step:

Understanding the Algorithm
The goal is to find two numbers in the array that sum up to a given target value. The hash map (dictionary) helps us to keep track of the numbers we've seen so far and their indices.
Here's a detailed breakdown of how the algorithm works:

Initialization:

We start by initializing an empty dictionary seen.
This dictionary will store the numbers we've encountered as keys and their corresponding indices as values.

Iterating Through the Array:

We iterate over the array using a loop. For each number in the array, we perform the following steps:

Calculate the Difference:

For each number at index i, we calculate the difference between the target value and the current number:
difference = Target - number.

Check the Dictionary:

We check if this difference is already in the dictionary seen.
If the difference is found, it means we have already seen a number that, when added to the current number, equals the target.
In this case, we return the indices of the two numbers.
If the difference is not found, it means we have not yet encountered a pair of numbers that add up to the target.
We then store the current number and its index in the dictionary.
Store the Current Number:

Regardless of whether we find the difference or not, we store the current number and its index in the dictionary. 
This ensures that all numbers encountered so far are available for future checks."""


def TwoSum (array, target):
    
    #creating a dict of seen difference
    seen = {}
    
    #iterate Through the array keeping track of values and index
    for index, value in enumerate(array):
        
        difference = target- value
        if difference in seen:
            return (seen[difference] , index)
            
        else:
            seen[value] = index
    return None


array = [3,2,4]    #Array is not sorted
target = 6
print(TwoSum(array, target))