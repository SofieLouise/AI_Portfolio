import random, math
from Lecture06 import queens_fitness

p_mutation = 0.2
num_of_generations = 30


def genetic_algorithm(population, fitness_fn, minimal_fitness):
    for generation in range(num_of_generations):
        print("Generation {}:".format(generation))
        print_population(population, fitness_fn)

        new_population = set()

        for i in range(len(population)):
            mother, father = random_selection(population, fitness_fn)
            child = reproduce(mother, father)

            if random.uniform(0, 1) < p_mutation:
                child = mutate(child)

            new_population.add(child)

        # Add new population to population, use union to disregard
        # duplicate individuals
        population = population.union(new_population)

        fittest_individual = get_fittest_individual(population, fitness_fn)

        if minimal_fitness <= fitness_fn(fittest_individual):
            break

    print("Final generation {}:".format(generation))
    print_population(population, fitness_fn)

    return fittest_individual


def print_population(population, fitness_fn):
    for individual in population:
        fitness = fitness_fn(individual)
        print("{} - fitness: {}".format(individual, fitness))


def reproduce(mother, father):
    '''
    Reproduce with two individuals with single-point crossover
    Return the child individual
    '''

    crossover_point = random.randint(0, len(mother) - 1)
    return mother[:crossover_point] + father[crossover_point:]


def mutate(individual):
    '''
    Mutate an individual by randomly assigning one of its bits
    Return the mutated individual
    '''
    individual = list(individual)
    i = random.randint(0, len(individual) - 1)
    individual[i] = random.randint(1, len(individual))
    return tuple(individual)


def random_selection(population, fitness_fn):
    """
    Compute fitness of each in population according to fitness_fn and add up
    the total. Then choose 2 from sequence based on percentage contribution to
    total fitness of population
    Return selected variable which holds two individuals that were chosen as
    the mother and the father
    """

    # Python sets are randomly ordered. Since we traverse the set twice, we
    # want to do it in the same order. So let's convert it temporarily to a
    # list.
    ordered_population = list(population)
    fitness_by_index = []
    total_fitness = 0
    for i in range(len(ordered_population)):
        fitness = fitness_fn(ordered_population[i])
        total_fitness += fitness
        fitness_by_index.append(fitness)

    fitness_ranges = []
    for i in range(len(ordered_population)):
        if total_fitness == 0:
            fitness_ranges.append(ordered_population[i])
        else:
            for j in range(int(fitness_by_index[i] / total_fitness * 100)):
                fitness_ranges.append(ordered_population[i])

    selected_individuals = []
    for i in range(2):
        selected_individual = fitness_ranges[random.randint(0, (len(fitness_ranges) - 1))]
        selected_individuals.append(selected_individual)
    return selected_individuals[0], selected_individuals[1]


def fitness_function(individual):
    return queens_fitness.fitness_fn_negative(individual)


def get_fittest_individual(iterable, func):
    return max(iterable, key=func)


def get_initial_population(n, count):
    '''
    Randomly generate count individuals of length n
    Note since its a set it disregards duplicate elements.
    '''
    return set([
        tuple(random.randint(0, 1) for _ in range(n))
        for _ in range(count)
    ])


def main():
    minimal_fitness = 0

    # Curly brackets also creates a set, if there isn't a colon to indicate a dictionary
    initial_population = {
        tuple(random.sample(range(1, 5), 4))
    }

    fittest = genetic_algorithm(initial_population, fitness_function, minimal_fitness)
    print('Fittest Individual: ' + str(fittest))


if __name__ == '__main__':
    main()
