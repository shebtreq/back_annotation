?UCBAdmissions
str(UCBAdmissions)
UCBAdmissions

#plot(UCBAdmissions)

margin.table(UCBAdmissions, 1)
margin.table(UCBAdmissions, 2)
margin.table(UCBAdmissions, 3)
margin.table(UCBAdmissions)

admit.dept <- margin.table(UCBAdmissions, 3)

admit.dept
str(admit.dept)
barplot(admit.dept)
prop.table(admit.dept)
round(prop.table(admit.dept), 2)

round(prop.table(admit.dept), 2)*100

