import math

def calculate_fitness_bf2(individual: list[float]) -> float:
    x1: float = individual[0]
    x2: float = individual[1]
    
    term_01: float = x1**2
    term_02: float = 2 * (x2**2)
    term_03: float = -0.3 * math.cos(3 * math.pi * x1) * math.cos(4 * math.pi * x2)
    
    return term_01 + term_02 + term_03 + 0.3
