#PF-Prac-21
def check_numbers(num1,num2):
    #start writing your code here
    num_list=[]
    for i in range(num1,num2+1):
        for j in range(num1,num2+1):
            if(i%j==0 and i not in num_list and i!=j):
                num_list.append(i)
    count=(len(num_list))
    return [num_list,count]

num1=2
num2=20
print(check_numbers(num1, num2))
