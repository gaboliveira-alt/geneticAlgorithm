def calculate_fitness_bf2(individual: list[float]) -> float:
    x1: float = individual[0]
    x2: float = individual[1]
    
    term_01: float = 2 * (x1**2)
    term_02: float = 1.05 * (x1**4)
    term_03: float = (x1**6) / 6
    term_04: float = x1 * x2
    term_05: float = x2**2
    
    return term_01 + term_02 + term_03 + term_04 + term_05
