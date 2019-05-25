#PF-Tryout
def sing_99_bottles():
   #start writing your code here
   for i in range(99,0,-1):
       print(i,end="")
       print(" bottles of bear on the wall, ",end="")
       print(i,end="")
       print(" bottles of beer.")
       print("Take one down, pass it around, ",end="")
       print(int(i-1),end="")
       print(" bottles of beer on the wall.")

               
sing_99_bottles()
