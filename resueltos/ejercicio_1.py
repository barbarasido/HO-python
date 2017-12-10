
print ("algo")
a=[x%5==0 and x%3==0 for x in range (1,1000)]
b=list()
for i in range (1,1000):
	if i%5==0 or i%3==0:
		b.append(i)
print(b)
sum=0
for i in b:
	sum=sum+i
print('la suma es ',sum)
