args <- commandArgs(TRUE)

print("Loading KnitR package")
library(package=knitr)

print("Knitting time!!!!!!!!!")
knit(args[1], args[2])
print("Knitting complete!!!!!")