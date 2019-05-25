def find_nine(nums):
    for i in range(0,len(nums)):
        if(nums[i]==9 and i<4):
            return True
    return False
    

nums=[1,9,4,5,6]
print(find_nine(nums))
