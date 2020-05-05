import sys

fasta=sys.argv[1]
gene=str(sys.argv[2]) #  e.g [gene=atpB] or simply atpB,  and  make sense only if fasta==yes. Key sensitive 

###################################################
#### generos presentes en toda la base de datos ###
###################################################


file=open("CLORO_SUMMARY.info","r")

lineas=[]

lista=[] 

dic_especie={} # from especie returns genera
dic_codigo={} #from species name return code
dic_genero={} #from genera returns list of species names
codigo_to_spp={} #from code return species name

for linea in file:
	lineas = lineas + [linea]
	
file.close()


for x in range(0, len(lineas)+1, 4):

	genero=lineas[x].split(".")[1].split(",")[0].split(" ")[1] #pq tengo un espacio adelante
	spp=lineas[x].split(".")[1].split(",")[0].split(" ")[2]
	especie=str(genero+"_"+spp)
		
	dic_especie[especie]=genero

	codigo=lineas[x+2].split(" ")[0]
	dic_codigo[especie]=codigo #si hay variantes de una misma especie, me quedo con el codigo de la ultima que lee.
	codigo_to_spp[codigo]=especie  
	
	if genero in dic_genero:	
		dic_genero[genero] = dic_genero[genero] + [especie]
	else:
		dic_genero[genero] = [especie]
			
#Its possible that some spp with subsp. pass the filter (len(dic_genero[genero])>=8) however there is only 22 subsp. 
#For this work we discarded subsp (they might carry some mild deleterious mutation that can inflate dn/ds)

########################################################################################
####### contando el numero de generos que tienen 8 o mas especies con genoma cloro #####
########################################################################################

for genero in dic_genero.iterkeys():
	
	if len(dic_genero[genero])>=8:
		
		print genero+'\t'+str(len(set(dic_genero[genero]))) #notar que evaluo len del conjunto pq hay especies repetidas.
		
		for especie in dic_genero[genero]:
		
			lista = lista + [dic_codigo[especie]]   #hago una lista de codigos
		
	else:
		
		continue


#############################################################################################
################################ armado del fasta #######################
#############################################################################################		

fasta_generos={} #keys would be the genera, items would be a list of dictionaries with fasta sequences of each species.

if fasta=="yes":

	file=open("CLORO_GENOMES.fasta","r")
	
	llave=False
	
	for linea in file:
		
		if linea[0]==">":
		
			codigo=linea.split("|")[1].split("cds")[0][:-1] #el cds esta siempre al parecer. Agarro hasta el menos uno pq antes del cds hay un barra baja. 
			
			if codigo in lista and gene in linea:
				especie=codigo_to_spp[codigo]
				genero=dic_especie[especie]
			
				if genero in fasta_generos: #if genera is already present it's because al least one species is present. 
					
					fasta_generos[genero][especie] = [">"+gene+"_"+especie+"_"+codigo+"\n"]

					llave=True
				
				if genero not in fasta_generos:
					fasta_generos[genero] = {}  #hay sola una especie por cada genero
					fasta_generos[genero][especie] = [">"+gene+"_"+especie+"_"+codigo+"\n"]

					llave=True

			else:
				llave=False
				continue
		
		elif llave==True:
			fasta_generos[genero][especie] = fasta_generos[genero][especie] + [linea]
			#print linea[:-1]
		
		else:
			continue

##############################################################################################
### for each genera, print a multifasta of the selected gene for the corresponding species ###
##############################################################################################

for genero in fasta_generos.iterkeys():
	
	file2=open(genero+"_"+gene+".txt", "w")
	
	for especie in fasta_generos[genero].iterkeys():
		
		for line in fasta_generos[genero][especie]:
			
			file2.write(line)
	
	file2.close()
	
################################################################################################
