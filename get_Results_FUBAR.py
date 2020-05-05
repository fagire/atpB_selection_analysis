import json
file2=open("RESULTS_SUMMARY","w")

dic={}

#expects a file with the filename of each hyphy results
file=open("hyphy_results_79","r")

files=[]

for linea in file:
	genero=linea.split('_')[0]
	dic[genero]=0
	file=open(linea[:-1],"r")
	data = json.load(file)
	
	file2.write(linea[:-1]+'\n')
	file2.write('\t'+"codon,alpha,beta,beta-alpha,Prob[alpha>beta],Prob[alpha<beta],BayesFactor[alpha<beta]"+"\n")
	for x in range(0,len(data["MLE"]["content"]["0"])):
		if data["MLE"]["content"]["0"][x][4] >= 0.90:
			alpha=float(data["MLE"]["content"]["0"][x][0])
			beta=float(data["MLE"]["content"]["0"][x][1])
			w=beta/alpha
			file2.write('\t'+str(x+1)+","+str(w)+","+str(data["MLE"]["content"]["0"][x])+'\n')
			dic[genero]=dic[genero]+1
	
	file.close()

file2.close()
        

for x in dic.iterkeys():
	print x+'\t'+str(dic[x])
