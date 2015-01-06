?state.area
data(state.area)
area <- state.area
area
hist(area)
boxplot(area)
summary(area)
mean(area)
median(area)
mean(area, trim=0.5)
sd(area)
mad(area)
IQR(area)
fivenum(area)
rm(list = ls())