import random
from fitness_function import calculate_fitness_cb3

def create_initial_population(population_size: int, lower_bound: float, upper_bound: float) -> list[list[float]]:
    population: list[list[float]] = []
    
    for _ in range(population_size):
        x1: float = random.uniform(lower_bound, upper_bound)
        x2: float = random.uniform(lower_bound, upper_bound)
        
        new_individual: list[float] = [x1, x2, 0.0]
        
        new_individual[2] = calculate_fitness_cb3(new_individual)
        
        population.append(new_individual)
    return population
