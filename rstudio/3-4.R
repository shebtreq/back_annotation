?quakes
quakes[1:5,]
mag <- quakes$mag
mag[1:5]

t.test(mag)

t.test(mag, alternative="greater", mu=4)

rm(list = ls())