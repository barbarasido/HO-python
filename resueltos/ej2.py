#( )"&=[]
import time
fibo=list( )
a=0
b=1
start=time.time( )
for i in range(100):
	if b>1000000:
		break
	else:
		fibo.append(b)
		suma=a+b
		a=b
		b=suma
	
sum=0
for i in range(len(fibo)):
	if fibo[i]%2==0:
		sum=sum+fibo[i]
print("la suma es ", sum)
stop=time.time( )
dura=stop-start
print(dura)
