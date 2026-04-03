import random
from fitness_function import calculate_fitness_bf2

number_vars: int = 2
lower_bound: float = -50.0
upper_bound: float = 50.0
population_size: int = 100

def create_initial_population() -> list[list[float]]:
    population: list[list[float]] = []
    
    for _ in range(population_size):
        x1: float = random.uniform(lower_bound, upper_bound)
        x2: float = random.uniform(lower_bound, upper_bound)
        
        new_individual: list[float] = [x1, x2, 0.0]
        
        new_individual[2] = calculate_fitness_bf2(new_individual)
        
        population.append(new_individual)
    return population
