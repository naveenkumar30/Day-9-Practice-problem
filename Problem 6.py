#PF-Prac-6
def list123(nums):
    #start writing your code here
    for i in range(0,len(nums)-1):
        if(nums[i]==1 and nums[i+1]==2 and nums[i+2]==3):
            return True
    return False

    

nums=[1,2,4,5]
print(list123(nums))
