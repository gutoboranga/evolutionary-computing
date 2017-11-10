data = read.table(file('shubert.txt'))
plot(data, axes=FALSE, type="o", col="blue", pch='', xlab="Generation", ylab="Result")

iterations = data[[1]]
results = data[[2]]

last_result = results[length(results)]
last_iteration = iterations[length(iterations)] + 1

ticks_rate = abs(last_result/5)

# eixo X
axis(1, at=10*0:last_iteration)

# eixo Y
axis(2, at=c(ticks_rate*0:last_result, last_result))

box()

title(main="Shubert: Evolution over generations")
