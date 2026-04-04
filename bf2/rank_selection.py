import random

def rank_selection(population: list[list[float]]) -> list[float]:
    sorted_population = sorted(population, key=lambda x: x[2])
    
    population_size = len(sorted_population)
    selection_weight = [population_size - i for i in range(population_size)]
    
    random_selection_individual = random.choices(sorted_population, weights=selection_weight, k=1)
    individual_selected = random_selection_individual[0]
    
    return list(individual_selected)
