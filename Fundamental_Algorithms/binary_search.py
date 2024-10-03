
#Binary Search takes a sorted array as an input as well as a target value
#It then returns the index of the value if it exists in the array


def binary_search(arr,target):

    left,right = 0, len(arr) - 1 #left and right points are established at the left and right ends of the array

    while left <= right: #the while loop will run so long as left never crosses over right
                         #if this occurs, it implies that the target value is not present in the array

        midpoint_index = left + (right-left) // 2 #Each round of the loop, "midpoint" is recalculated
                                                  #The search area will get smaller and smaller with each iteration
                                                  #Until the value is found or determined to not be present

        if arr[midpoint_index] == target: #if the value as index "midpoint" equal the target, we return the midpoint index
            print(f"the value {target} is located at index {midpoint_index}")
            return midpoint_index

        elif arr[midpoint_index] < target: #if the value at mid point index is less than the target, it implies
                                           #that the target is in the right half of the search area, and so
                                           #the 'left' point is moved up to the position just to the right of midpoint
                                           #this moves the search area to the region where we know the target must be
            left = midpoint_index + 1

        elif arr[midpoint_index] > target: #Similarly, if the value are midpoint is greater than the target
                                           #it implies that the value is in the left half of the search area
                                           #and so the 'right' pointer is repositioned just to the left of midpoint
            right = midpoint_index - 1
#This continues until the value at midpoint is equal to the target or until it becomes clear that it is not present
#in the array
    print("this array does not contain the target value")
    return -1
#This logic is obviously only relevant to a sorted array. It will not deliver the index location of values
#for unsorted arrays 

nums = [4,6,8,13,15,17,22,34,40]

binary_search(nums,13)