import random

def apply_mutation(individual: list[float], lower_bound: float, upper_bound: float) -> list[float]:
    if random.random() < 0.35:
        gene_to_mutate: int = random.randint(0, 1)
        individual[gene_to_mutate] = random.uniform(lower_bound, upper_bound)
        individual[2] = 0.0
    return individual