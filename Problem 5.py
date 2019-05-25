#PF-Prac-5
def count_digits_letters(sentence):
    #start writing your code here
    sentence.lower()
    a=0
    d=0
    l=[]
    for c in sentence:
        if(c.isalpha()):
            d=d+1
        elif(c.isdigit()):
            a=a+1
    l.append(d)
    l.append(a)
    return l
    

    

    
    #return result_list

sentence="Infosys 123"
print(count_digits_letters(sentence))
