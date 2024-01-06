n = 20
c1=0
c2 = 0
for i in range(0,n):
    c=1
    
    for j in range(0,i):
        
        if i==0 or j==0 :
            print(chr(65), end=" ")
        elif j==i-1 and i<n-1:
            print(chr(66+c1), end =" ")
            c1+=1
        elif i==n-1 :
            print(chr(65+c), end = " ")
            c+=1
        else:
            print(" ", end =" ")
    
       
    print()
            
        
    

