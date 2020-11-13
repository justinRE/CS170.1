import math
def ListSqrRoot(nums):
    n=len(nums)
    for i in range(n):
        nums[i]=math.sqrt(nums[i])
        

def main():
    nums=eval(input("Please enter a list of numbers:"))
    print( "Before calling the function your list is:")
    print (nums)
    ListSqrRoot(nums)
    print ("After calling the function your list is:")
    print (nums)

main()
