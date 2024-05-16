import numpy as np

def F(x):
    """The function to be maximized."""
    return 4 + 2*x + 2*np.sin(20*x) - 4*x**2

def fitness_proportional_selection(population, fitness_values):
    """Selects an individual from the population based on fitness-proportional selection."""
    total_fitness = sum(fitness_values)
    probabilities = [f / total_fitness for f in fitness_values]
    return np.random.choice(population, p=probabilities)

def mutate(x, epsilon=0.01):
    """Mutates the individual x by a small value epsilon."""
    mutation_type = np.random.choice(['decrease', 'copy', 'increase'], p=[0.3, 0.4, 0.3])
    if mutation_type == 'decrease':
        return max(0, x - epsilon)
    elif mutation_type == 'increase':
        return min(1, x + epsilon)
    else:
        return x

def crossover(x, y):
    """Performs crossover between two individuals x and y."""
    a = np.random.uniform(0, 1)
    return a * x + (1 - a) * y

def run_experiment(N=10, generations=100, epsilon=0.01):
    """Runs the evolutionary algorithm experiment."""
    # Initialize population
    population = np.array([0.01*k for k in range(101)])
    best_fitness_over_time = []

    for generation in range(generations):
        # Calculate fitness for each individual
        fitness_values = np.array([F(x) for x in population])

        # Selection
        selected = []
        for _ in range(N):
            selected_individual = fitness_proportional_selection(population, fitness_values)
            selected.append(selected_individual)

        # Crossover and Mutation
        new_population = []
        for _ in range(N):
            # Recalculate fitness for selected individuals
            selected_fitness_values = np.array([F(x) for x in selected])
            parent1 = fitness_proportional_selection(selected, selected_fitness_values)
            parent2 = fitness_proportional_selection(selected, selected_fitness_values)
            offspring = crossover(parent1, parent2)
            offspring = mutate(offspring, epsilon)
            new_population.append(offspring)

        population = np.array(new_population)

        # Track the best fitness over time
        best_fitness_over_time.append(max(fitness_values))

    # Calculate final fitness values
    final_fitness_values = np.array([F(x) for x in population])
    best_individual = population[np.argmax(final_fitness_values)]
    best_fitness = np.max(final_fitness_values)

    return best_individual, best_fitness, best_fitness_over_time

# Run the experiment
best_individual, best_fitness, best_fitness_over_time = run_experiment()
print("Best Individual:", best_individual)
print("Best Fitness:", best_fitness)
print("Best Fitness over time: ", best_fitness_over_time)
