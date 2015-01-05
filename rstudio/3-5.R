?HairEyeColor
str(HairEyeColor)

margin.table(HairEyeColor, 2)

eyes <- margin.table(HairEyeColor, 2)
eyes
round(prop.table(eyes), 2)

chi1 <- chisq.test(eyes)
chi1
str(chi1)


chi2 <- chisq.test(eyes, p = c(.41, .32, .15, .12))

chi2

rm(list = ls())