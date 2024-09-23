
def twoSum(nums, target):
    visited_hash = {}


    for index,num in enumerate(nums):
        sum_check = target - num
        if sum_check in visited_hash:
           return [visited_hash[sum_check],index]
        else:
            visited_hash[num] = index

print(twoSum([3,5,9,7,1,2], 16))

#we are asked to find and return the indices of the two numbers in a list that add up to the target number
#We first create an empty hashtable, we then use enumerate to loop through the list

#the enumerate function, when called on a collection, keeps track of both the value and the index
#We check to see if k minus the current value is present in the hashtable.
#If it is, we return a list containing the index of the k-num value and the index of the current value

#if k minus the current value is not a key in the dictionary, we save the current value as a key in the dictionary
#with the index as its value

#As we iterate over the list, if k - current value is one of the value we've stored, then that means we've
#at some point, encountered a number in the list that would add to the current value to equal target/k
#Once establishing this, we can simply return the indices of both values.

