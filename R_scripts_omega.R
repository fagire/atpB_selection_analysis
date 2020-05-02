omegaB <- read.delim("~/Desktop/Cloroplastos/TODO/generas/atpB/RESULTS/DISTRIBUTION/sitios_y_omega", header=FALSE)
omegaA <- read.delim("~/Desktop/Cloroplastos/TODO/generas/atpA/RESULTS/DISTRIBUTION/sitios_y_omega", header=FALSE)


ks.test(omegaB$V2, omegaA$V2, alternative = c("greater"), exact = NULL)
#chequea si la primera es mas grande que la segunda.
#no se puede descartar hipotesis nula - que son iguales -

############
ks.test(c(1,2,3,4,5,6,7,8,9), c(42,23,46,33,45,344,55,31,554), alternative = c("greater"), exact = NULL)
#pvalue significativo. 
ks.test( c(42,23,46,33,45,344,55,31,554),c(1,2,3,4,5,6,7,8,9), alternative = c("greater"), exact = NULL)
#pvalue no significativo
#la que esta por debajo tiene valores en la distr. mas grande. 
############


library("ggplot2")#, lib.loc="~/R/x86_64-pc-linux-gnu-library/3.3")

################DENSITY###############3
carrots <- data.frame(w=omegaA$V2)
cukes <- data.frame(w=omegaB$V2)

#Now, combine your two dataframes into one.  First make a new column in each.
carrots$genes <- 'atpA'
cukes$genes <- 'atpB'

# #le cambio el nombre del maldito data frame para que corra
# colnames(carrots)[1] <- "dist_gen"
# colnames(cukes)[1] <- "dist_gen"

#and combine into your new data frame vegLengths
vegLengths <- rbind(carrots, cukes)


#now make your lovely plot
ggplot(vegLengths, aes(w, fill = genes, color=genes)) + geom_density(alpha = 0.2)

#malditos colores
dist_part <- data.frame(w=omegaB$V2)
dist_gen <- data.frame(w=omegaA$V2)

ggplot() + geom_density(aes(x=w), colour="red", fill="red", data=dist_part, alpha = 0.2) + geom_density(aes(x=w), colour="blue",fill="blue",data=dist_gen, alpha = 0.2)

#########probando diferentes mierdas ############# no puedo hacer que queden barritas con valores relativos de freq.
ggplot(vegLengths, aes(w, fill = genes)) + geom_histogram(alpha = 0.5, aes(y = ..density..),binwidth = 1, position = 'identity')

ggplot(vegLengths, aes(w, fill = genes)) + geom_density(alpha = 0.5, aes(y = ..scaled..), position = 'identity')

ggplot(vegLengths, aes(w, fill = genes)) + geom_histogram(alpha = 0.5, aes(y = ..density..), position = 'identity') + geom_density(alpha = 0.2)

ggplot(vegLengths, aes(w, fill = c(c("red"),c("blue")), color=c(c("red"),c("blue")))) + geom_histogram(alpha = 0.5, aes(y = ..density..), binwidth = 2, position = 'identity') + geom_density(alpha = 0.2)

hist(omegaB$V2, breaks=20)
hist(omegaA$V2, breaks=20)


DF1 <- data.frame(x = omegaB$V2) #rnorm(1000))

ggplot(DF1, aes(x = x)) +
  geom_histogram(aes(y = ..density.. * 0.2),
                 binwidth = 0.5, fill = "blue") +
  ylab("Relative frequency")
