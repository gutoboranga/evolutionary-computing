from sys import argv

from genetic import genetic
from functions import drop_wave, shubert, six_hump_camel_back


if argv[1] == "shubert":
    result = genetic(shubert)

elif argv[1] == "drop_wave":
    result = genetic(drop_wave)
    
best_solution = result[0]
best_value = result[1]

print("\nMelhor resultado: {}".format(best_value))
print("x1 = {}\nx2 = {}".format(best_solution[0], best_solution[1]))
