num=600851475143 
x=num
fac=2
while x!=1:
    while x/fac==int(x/fac):
        x=x/fac
    else:
        fac+=1      
        
fac=fac-1        
print("el factor es ", fac)
