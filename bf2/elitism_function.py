def get_the_better(population: list[list[float]], size: int = 2) -> list[list[float]]:
    sorted_individual = sorted(population, key=lambda x: x[2])
    return [list(individual) for individual in sorted_individual[:size]]