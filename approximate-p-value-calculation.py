import random

dic={}
Y = 1 
count2 = 0

for y in range(1,10001): #e.g. ten thousands simulation
	#print y
	dic={}
	for x in range(1, 45): #e.g. 45 selective instances (= total number of sites under selection). Balls
		#print x
		cajita=random.randrange(1,36,1) #e.g. 36 different sites under selection. Bin
		if cajita not in dic:
			dic[cajita] = 1
		else:
			dic[cajita] = dic[cajita] + 1
	
	
	count = 0
	for x in dic.iterkeys():
			if dic[x] >= 2:  # i.e. one bin with X one or more balls ball # significa que una cajita tiene X o mas pelotitas
				count = count + 1
	
	if count >= Y: # i.e Y or more bins hava X or more balls.  #significa que Y o mas cajitas tienen X o mas pelotitas. 
		count2 = count2 + 1
	else:
		continue
	

print float((count2*1.0)/(10000))


