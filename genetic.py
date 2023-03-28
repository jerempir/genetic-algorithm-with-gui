import random


def fitness(x):
    return (4*(x[0]-5)**2 + (x[1]-6)**2)

def fitness1(x):
    return (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2

def generate_individual():
    individual = []
    individual.append(random.uniform(population_value[0], population_value[1]))
    individual.append(random.uniform(population_value[0], population_value[1]))
    return individual

def crossover(parent1, parent2):
    individual = []
    individual.append((parent1[0] + parent2[0]) / 2)
    individual.append((parent1[1] + parent2[1]) / 2)
    return individual

def mutate(individual):
    individual[0] += random.uniform(-1, 1)
    individual[1] += random.uniform(-1, 1)
    return individual

population_size = 50
population_value = [-50, 50]
generations = 10000

# Initialize population
population = [generate_individual() for i in range(population_size)]

for generation in range(generations):
    # Evaluate fitness function
    fitness_scores = [fitness(individual) for individual in population]

    # Select parents
    parents = random.choices(population, weights=fitness_scores, k=2)

    # Create offspring
    offspring = crossover(parents[0], parents[1])
    offspring = mutate(offspring)

    # Replace worst individual in population with offspring
    worst_index = fitness_scores.index(max(fitness_scores))
    population[worst_index] = offspring

for i in range(len(fitness_scores)):
    print(i,fitness_scores[i],population[i])
# Get best individual
best_individual = min(population, key=fitness)

print("Minimum found:", best_individual)
