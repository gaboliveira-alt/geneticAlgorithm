from fitness_function import calculate_fitness_bf2
from population import create_initial_population
from elitism_function import get_the_better
from rank_selection import rank_selection
from mutation import apply_mutation
from crossover import crossover

MAX_GENERATIONS: int = 1000
TOTAL_RUNS: int = 100
ELITISM_SIZE: int = 2
POPULATION_SIZE: int = 100
LOWER_BOUND: float = -50.0
UPPER_BOUND: float = 50.0
SUCCESS_THRESHOLD: float = 0.01

def run_genetic_algorithm() -> tuple[bool, int]:
    nfe_count: int = 0
    
    current_population = create_initial_population(POPULATION_SIZE, LOWER_BOUND, UPPER_BOUND)
    nfe_count += POPULATION_SIZE
    
    for _ in range(MAX_GENERATIONS):
        current_population.sort(key=lambda better: better[2])
        best_individual = current_population[0]
        
        if abs(best_individual[2] - 0.0) < SUCCESS_THRESHOLD:
            return (True, nfe_count)
        
        new_population = get_the_better(current_population, ELITISM_SIZE)
        
        while len(new_population) < POPULATION_SIZE:
            parent_01 = rank_selection(current_population)
            parent_02 = rank_selection(current_population)
            
            child = crossover(parent_01, parent_02)
            child = apply_mutation(child, LOWER_BOUND, UPPER_BOUND)
            
            child[2] = calculate_fitness_bf2(child)
            nfe_count += 1
            
            new_population.append(child)
        current_population = new_population
    return (False, nfe_count)
