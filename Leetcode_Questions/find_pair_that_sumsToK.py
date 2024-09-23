def findPair(arr, k):
    arr.sort()
    left, right = 0, len(arr) -1

    while left < right:
        if arr[left] + arr[right] == k:
            return True
        elif arr[left] + arr[right] < k:
            left +=1
        elif arr[left] + arr[right] > k:
            right -=1
    return False

#the function searches an array for two numbers that sum to k
#it returns true if two such numbers are found and false if they are not

#the function starts by sorting the array in ascending order
#it then sets up pointers at either end of the array
#if the sum of the numbers at the position of each pointer is less than k, it increments the left pointer, making the sum-pair larger
#if the sum of the numbers at the position of each pointer is greater than k, it decrements the right pointer, making the sum-pair smaller

#print(findPair([4,5,1,-3,6,2],11))
#The findPair function solves the problem with O(nlogn) time complexity, because of the sort function
#We can however solve the problem with an O(n) complexity using a dictionary, or hashtable

def findPairHash(arr,k):
    hash = {}
    for i in arr:
        sum_check = k-i
        if sum_check in hash:
            return True
        else:
            hash[i] = True
    return False

print(findPairHash([4,5,1,-3,1,2],9))

#The function creates an empty dictionary, then iterates through the list only once
# it checks to see if k minus the current i is present in the dictionary
# if it is, it returns true
# if it is not, it stores the current i in the dictionary, and repeats with the next value of 'i'
# if at any point, k-i is present in the dictionary, it means that we've previously come into contact
# with a number that would sum to k if added to the current value of i

#this has a time complexity of O(n) because it is only dependent on how long the list is
