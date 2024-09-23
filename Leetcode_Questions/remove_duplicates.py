
#write an algorithm that removes duplicate elements from an array and returns an array of unique elements
#There are three ways to do this

#1. brute force method

def removeDuplicatesBrute(arr):
    return_arry = []

    for i in arr:
        if i not in return_arry:
            return_arry.append(i)
    return return_arry


print(removeDuplicatesBrute([1,3,4,3,9,6,4,4,3,1,7,8,4,7]))
#The brute force algorithm defines an empty list
#It then iterates through the array, checking if each array element already exists in the list.
#if the array element is not found in the new list, it is appended to the list.
#The new list of only unique values is then returned
#The problem with this, is that we have to keep iterating through 'return_arry' to check for the presence of values
#this combined with the main iteration creates the same effect as a set of imbedded loops
#The time complexity is therefore O(n^2)



#2. Sorting Method

def removeDuplicatesSorting(arr):
    arr.sort()
    return_arry = []

    for i in range(len(arr)):
        if arr[i] != arr[i-1]:
            return_arry.append(arr[i])
    return return_arry

print(removeDuplicatesSorting([1,3,4,3,9,6,4,4,3,1,7,8,4,7]))

#this method first sorts the elements in ascending order, so repeates end up grouped together
#it then iterates through the array, checking if each element is the same as the element before it
#if an element is not the same as the element before it, it is added to 'return_arry', 'return_arry' is then returned
#Sorting is the most time intensive operation here, python sort has a time complecity of o(nlogn)


#3. Hash Table Method

def removeDuplicatesHash(arr):
    visited = {}
    return_arry = []
    for i in arr:
        if i not in visited:
            visited[i] = True
            return_arry.append(i)
    return return_arry

#this method iterates through the array, saving elements to a dictionary if they've yet to be encountered
#it uses this comparison as a basis for whether or not to append the element to 'return_arry'
#if it already exists in the dictionary, we do not append.
#searching through a dictionary is done in constant O(1) time
#The time complexity is completely dependent then on the length of the array
#time complexity is O(n)






