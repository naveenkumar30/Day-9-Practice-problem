#PF-Prac-11
def find_upper_and_lower(sentence):
    #start writing your code here
    a=0
    b=0
    for i in sentence:
        if(i>="a"and i<="z"):
            b=b+1
        if(i>="A" and i<="Z"):
            a=a+1
    l=[]
    l.append(a)
    l.append(b)
    
       
    return l

sentence="Come Here"
print(find_upper_and_lower(sentence))
