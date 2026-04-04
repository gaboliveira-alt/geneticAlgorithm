def crossover(parent_01: list[float], parent_02: list[float]) -> list[float]:
    cross_rate = 0.96
    
    child_x1 = (parent_01[0] * cross_rate) + (parent_02[0] * (1 - cross_rate))
    child_x2 = (parent_02[1] * cross_rate) + (parent_02[1] * (1 - cross_rate))
    
    return [child_x1, child_x2, 0.0]
