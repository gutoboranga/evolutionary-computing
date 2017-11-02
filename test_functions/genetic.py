from random import randint, uniform

from functions import drop_wave, shubert


INITIAL_X1 = 5.12
INITIAL_X2 = 5.12

POPULATION_SIZE = 10
SOLUTIONS_TO_KEEP_IN_POPULATION = 5

MAX_ITERATIONS = 10


def genetic(function):
    iteration = 0
    
    population = generate_initial_population()
    values = []
    
    while iteration < MAX_ITERATIONS:
        # calculate result value for each solution in population
        values = apply_function(population, function)
        
        print('================== ITERACAO ' + str(iteration) + '==================\n\n')
        for i in range(0, POPULATION_SIZE - 1):
            print(str(population[i]) + ': ' + str(values[i]))
            print('\n')
        
        # filter best solutions in population, reproduce and mutate
        population = choose_best_solutions(population, values)
        population = generate_descendants(population)
        population = mutate(population)
        
        # best = find_best_solution(population, values)
        # print(best)
        
        iteration += 1
    
    best = find_best_solution(population, values)
    
    return best


def generate_initial_population():
    population = []
    
    for i in range(0, POPULATION_SIZE - 1):
        x1 = uniform(0, INITIAL_X1)
        x2 = uniform(0, INITIAL_X2)
        
        new_item = (x1, x2)
        
        population.append(new_item)
        
    return population

def apply_function(population, function):
    values = []
    
    for item in population:
        v = function(item[0], item[1])
        values.append(v)
        
    return values

def choose_best_solutions(population, values):
    top_population = []
    
    for i in range(0, SOLUTIONS_TO_KEEP_IN_POPULATION):
        best = find_best_solution(population, values)
        
        population.remove(best[0])
        values.remove(best[1])
        
        top_population.append(best[0])
        
    return top_population

def generate_descendants(population):
    number_of_descendants_to_create = POPULATION_SIZE - SOLUTIONS_TO_KEEP_IN_POPULATION
    
    for i in range(0, number_of_descendants_to_create):
        parents = choose_random_parents(population)
        
        child = reproduce(parents)
        
        population.append(child)
    
    return population

def choose_random_parents(population):
    index0 = randint(0, SOLUTIONS_TO_KEEP_IN_POPULATION - 1)
    index1 = randint(0, SOLUTIONS_TO_KEEP_IN_POPULATION - 1)
    
    return [population[index0], population[index1]]

def reproduce(parents):
    parent0 = parents[0]
    parent1 = parents[1]
    
    # calculates mean of parents x1 and x2
    x1 = (parent0[0] + parent1[0]) / 2
    x2 = (parent0[1] + parent1[1]) / 2
    
    return (x1, x2)

def mutate(population):
    return population
    
def find_best_solution(population, values):
    best_value = values[0]
    best_solution = population[0]
    
    for i in range(0, len(values)):
        if values[i] < best_value:
            best_value = values[i]
            best_solution = population[i]
        
    return [best_solution, best_value]

# usage example:
result = genetic(shubert)

best_solution = result[0]
best_value = result[1]

print("Melhor resultado: {}".format(best_value))
print("Valores: x1={}, x2={}".format(best_solution[0], best_solution[1]))
