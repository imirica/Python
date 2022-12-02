#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#input (what) : nums (array) + target (integer)
#output : indices of array (integers)

arr=[]

while True:
    try:
        n=int(input("How many elements should contain the array? :"))
        for i in range(n):
            element=int(input("enter the element :"))
            arr.append(element)
        target=int(input("Enter a target : "  ))
        break
    
    except ValueError:
        print("invalid input, try again!")


def two_sum(arr, target):
    
    #use two pointers - left and right
    left=0
    right= len(arr)-1
    
    #add the elements of the array associated with its pointers
    while left<right:
        
        #if the sum of the element == the target => the left and right
        if arr[left] + arr[right] == target:
            return left, right
            break
        
        #if the sum is greater than the terget, right pointer moves to the left ( decreases with one)
        if arr[left] + arr[right] > target:
            right-=1
            
        #if the sum is lower than the target , left pointer increases with one
        if arr[left] + arr[right] < target:
            left +=1
    
print(two_sum(arr,target))
