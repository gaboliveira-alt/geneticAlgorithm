from fitness_function import calculate_fitness_cb3
from population import create_initial_population
from elitsm_function import get_the_better
from rank_selection import rank_selection
from mutation import apply_mutation
from crossover import crossover

MAX_GENERATIONS: int = 1000
TOTAL_RUNS: int = 100
ELITISM_SIZE: int = 2
POPULATION_SIZE: int = 100
LOWER_BOUND: float = -5.0
UPPER_BOUND: float = 5.0
SUCCESS_THRESHOLD: float = 0.01

def run_genetic_algorithm() -> tuple[bool, int]:
    nfe_tax: int = 0
    
    current_population = create_initial_population(POPULATION_SIZE, LOWER_BOUND, UPPER_BOUND)
    nfe_tax += POPULATION_SIZE
    
    for _ in range(MAX_GENERATIONS):
        current_population.sort(key=lambda better: better[2])
        best_individual = current_population[0]
        
        if abs(best_individual[2] - 0.0) < SUCCESS_THRESHOLD:
            return (True, nfe_tax)
        
        new_population = get_the_better(current_population, ELITISM_SIZE)
        
        while len(new_population) < POPULATION_SIZE:
            parent_01 = rank_selection(current_population)
            parent_02 = rank_selection(current_population)
            
            child = crossover(parent_01, parent_02)
            child = apply_mutation(child, LOWER_BOUND, UPPER_BOUND)
            
            child[2] = calculate_fitness_cb3(child)
            nfe_tax += 1
            
            new_population.append(child)
        current_population = new_population
    return (False, nfe_tax)


if __name__ == "__main__":
    success_count: int = 0
    total_nfe: int = 0
    
    print(f'Iniciando {TOTAL_RUNS} execuções....')
    
    for i in range(TOTAL_RUNS):
        is_success, run_nfe = run_genetic_algorithm()
        
        if is_success:
            success_count += 1
        total_nfe += run_nfe
        
        if (i + 1) % 10 == 0:
            print(f'Progresso {i + 1}/{TOTAL_RUNS} execuções concluidas.')
    
    success_rate: float = (success_count / TOTAL_RUNS) * 100
    average_nfe: float = total_nfe / TOTAL_RUNS
    
    print("\n" + "="*40)
    print("         RESULTADOS FINAIS")
    print("="*40)
    print("Problema: Camel Back - 3 Three Hump (CB3)")
    print(f"Taxa de Sucesso (SR): {success_rate:.2f}%")
    print(f"Média de NFE: {average_nfe:.2f}")
    print("="*40)
