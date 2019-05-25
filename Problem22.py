#PF-Tryout
def diagonal_stars(number):
    for i in range(0,number):
        for j in range(i):
            print(".",end='')
        print("*")
        
   #start writing your code here

number=6    
diagonal_stars(number)
