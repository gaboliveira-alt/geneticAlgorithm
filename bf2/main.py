from genetic_algorithm import run_genetic_algorithm, TOTAL_RUNS


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
    print("Problema: Bohachevsky 2 (BF2)")
    print(f"Taxa de Sucesso (SR): {success_rate:.2f}%")
    print(f"Média de NFE: {average_nfe:.2f}")
    print("="*40)
