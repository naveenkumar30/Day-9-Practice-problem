#PF-Prac-31
def sum_of_elements(num_list,number):
    a=len(num_list)
    s=0
    for i in range(1,a-1):
        if(num_list[i-1]!=number and num_list[i+1]!=number and num_list[i]!=number):
            s=s+num_list[i]
    if(num_list[1]!=number and num_list[0]!=number):
        s=s+num_list[0]
    if(num_list[a-2]!=number and num_list[a-1]!=number):
        s=s+num_list[a-1]
    return s
    
    

num_list=[1,2,1,2]
number=2
print(sum_of_elements(num_list, number))
