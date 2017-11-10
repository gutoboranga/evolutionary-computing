data = read.table(file('results/drop_wave_zoom.txt'))
plot(data, axes=FALSE, type="o", col="blue", lwd=2, pch='', xlab="Generation", ylab="Result")

iterations = data[[1]]
results = data[[2]]

first_result = results[1]
last_result = results[length(results)]

last_iteration = iterations[length(iterations)] + 1

y_ticks_rate = abs((last_result - first_result)/5)

# eixo X
axis(1, at=10*0:last_iteration)

# eixo Y
axis(2, at=seq(first_result, last_result, by=-y_ticks_rate))

box()

title(main="Drop Wave: Evolution over generations (zoom)")
