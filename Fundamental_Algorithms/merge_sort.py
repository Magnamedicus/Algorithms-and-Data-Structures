

def merge_sort(arr):

    def merge(lst1,lst2):

        combined = []
        p1,p2 = 0,0

        while p1 < len(lst1) and p2 < len(lst2):
            if lst1[p1] < lst2[p2]:
                combined.append(lst1[p1])
                p1 += 1
            else:
                combined.append(lst2[p2])
                p2 += 1

        while p1 < len(lst1):
            combined.append(lst1[p1])
            p1 +=1

        while p2 < len(lst2):
            combined.append(lst2[p2])
            p2 +=1

        return combined

    if len(arr) == 1:
        return arr

    midpoint = len(arr) // 2

    left = merge_sort(arr[:midpoint])
    right = merge_sort(arr[midpoint:])

    return merge(left,right)



nums = [4,7,2,4,1,9,4,6,100,81,22,30,18,1]

print(merge_sort(nums))


#classic divide and conquer sorting algorithm with O(nlogn) time complexity.
#The function first defines a 'merge' function designed to join two sorted lists to create a single sorted list
#merge() creates a new list "combined" and then uses pointers to compare values in each list, appending them in ascending order

#Merge_sort itself is recursively called on half-slices of the input list, breaking the lists into smaller and smaller left and right chunks
#This continues until a base case is reached of each list containing only one element

#at this point, the call stack begins unwinding, where merge() is called on each 1 element list, and then each two element list, and so on
#it's necessary to break the lists into one element because a one element list is technically sorted and merge() requires its inputs
#to be sorted lists. 