Fubar_results <- read.csv("~/Desktop/Cloroplastos/Datos1 - Sheet1.csv")

col<- colorRampPalette(c("black", "red", "white"))(256)
heatmap(as.matrix(Fubar_results[,2:3]),labRow = Fubar_results[,1], scale="column", col=col)



library(reshape2)
melted_data <- melt(Fubar_results)


#melted_data[order(melted_data$value),]

melted_data$value <- with(melted_data,factor(value,levels = rev(sort(unique(value)))))



library(ggplot2)
ggplot(melted_data, aes(x=variable, y=X, fill= value)) + geom_tile()



library(pheatmap)
pheatmap(Fubar_results[,2:3])