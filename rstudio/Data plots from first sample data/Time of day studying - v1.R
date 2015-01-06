rm(list=ls())

dump <- read.csv("~/Desktop/Classified/classroom_dataset.csv", header = TRUE, sep ='\t')
dump.height <- dim(dump)[1]
dump.width <- dim(dump)[2]

rownames(dump) <- NULL


index <- seq(from = 1, length.out = dump.height)
dump <- data.frame(Index = index, dump[1:dump.height, 1:dump.width])
dump.width <- dim(dump)[2]

dump.loaded <- dump[ with(dump, grepl("LOADED", payload)), ]
dump.loaded.time <- subset(dump, selec = c("id..received"))


videotimearray <- c(NULL)
length = dim(dump.loaded.time)[1]
for(i in 1:10000)
{
  date <- as.character(dump.loaded.time[i,1])
  time <- as.character(as.data.frame(strsplit(date,' '))[2,1])
  hours <- as.numeric(as.character(as.data.frame(strsplit(time,':'))[1,1]))
  minutes <- as.numeric(as.character(as.data.frame(strsplit(time,':'))[2,1]))
  seconds <- as.numeric(as.character(as.data.frame(strsplit(time,':'))[3,1]))
  
  exacthour <- hours + minutes/60 + seconds/3600
  videotimearray <- union(videotimearray, c(exacthour))
  #message("exact hour:", exacthour)
}

hist(videotimearray,breaks=24,xlim=c(0,24), main="Time of day students study", col="skyblue", xlab="Time Of Day", ylab="Frequency", border="blue")

