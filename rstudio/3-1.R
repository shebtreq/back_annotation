groups <- c(rep("blue", 3990),
            rep("red", 4140),
            rep("orange",1890),
            rep("green", 3770),
            rep("purple", 855))

groups.t1 <- table(groups)
groups.t1

groups.t2 <- sort(groups.t1, decreasing = TRUE)
groups.t2

prop.table(groups.t2)

round(prop.table(groups.t2), 2)

round(prop.table(groups.t2), 2)*100








